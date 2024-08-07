from rest_framework.decorators import api_view
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import SpecialOfferModel
from .serializers import SpecialOfferSerializer

channel_layer = get_channel_layer()

@api_view(['POST'])
def create_offer(request):
    serializer = SpecialOfferSerializer(data=request.data)
    if serializer.is_valid():
        title = request.data.get('title')
        new_price = request.data.get('newPrice')
        serializer.save()
        async_to_sync(channel_layer.group_send)(
            'online',
            {
                'type': 'send_offer_notification',
                'message': f'Limited Offer on:\n {title} for only : {new_price} !'
            }
        )
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_offers(request):
    offer = SpecialOfferModel.objects.all()
    serializer = SpecialOfferSerializer(offer, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def search_offer(request):
    title = request.data.get('title')
    category = request.data.get('category')

    try:
        offer = SpecialOfferModel.objects.get(title=title, category=category)
        serializer=SpecialOfferSerializer(offer)
    except SpecialOfferModel.DoesNotExist:
        return Response({'message': 'Offer not found.'}, status=404)

    return Response(serializer.data, status=200)

@api_view(['DELETE'])
def delete_offer(request):
    title = request.data.get('title')
    category = request.data.get('category')

    try:
        offer = SpecialOfferModel.objects.get(title=title, category=category)
    except SpecialOfferModel.DoesNotExist:
        return Response({'message': 'Offer not found.'}, status=404)

    offer.delete()

    return Response({'message': 'Offer deleted successfully.'}, status=200)
