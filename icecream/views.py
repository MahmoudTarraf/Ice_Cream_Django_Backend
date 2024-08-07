from rest_framework.decorators import api_view
from rest_framework.response import Response

from icecream.models import IceCreamModel
from .serializers import IceCreamSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@api_view(['POST'])
def create_icecream(request):
    serializer = IceCreamSerializer(data=request.data)
    if serializer.is_valid():
        title = request.data.get('title')
        price = request.data.get('price')
        serializer.save()
        async_to_sync(channel_layer.group_send)(
            'online',
            {
                'type': 'send_ice_cream_notification',
                'message': f'New ice cream is available:\n {title} for only : {price} !'
            }
        )
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_all_icecream(request):
    icecream = IceCreamModel.objects.all()
    serializer = IceCreamSerializer(icecream, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def search_ice_cream(request):
    title = request.data.get('title')
    category = request.data.get('category')

    try:
        ice_cream = IceCreamModel.objects.get(title=title, category=category)
        serializer=IceCreamSerializer(ice_cream)
    except IceCreamModel.DoesNotExist:
        return Response({'message': 'Ice cream not found.'}, status=404)

    return Response(serializer.data, status=200)

@api_view(['PUT'])
def update_ice_cream(request, ice_cream_id):
    try:
        ice_cream = IceCreamModel.objects.get(id=ice_cream_id)
    except IceCreamModel.DoesNotExist:
        return Response({'message': 'Ice cream not found.'}, status=404)

    serializer = IceCreamSerializer(ice_cream, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Ice cream updated successfully.'}, status=200)
    else:
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def delete_ice_cream(request):
    title = request.data.get('title')
    category = request.data.get('category')

    try:
        ice_cream = IceCreamModel.objects.get(title=title, category=category)
    except IceCreamModel.DoesNotExist:
        return Response({'message': 'Ice cream not found.'}, status=404)

    ice_cream.delete()

    return Response({'message': 'Ice cream deleted successfully.'}, status=200)

@api_view(['GET'])
def welcome(request):
    this_response={
        'path(createicecream/)' : 'views.create_icecream)',
        'path(geticecreams/)': 'views.get_all_icecream)',
        'path(login)':'(views.login)',
        'path(signup)':'(views.signup)',
        'path(getuser/<str:identifier>)':'(views.get_user)',
        'path(createanoffer/)':'(views.create_offer)',
        'path(getalloffers/)':'(views.get_all_offers)',
    }
    return Response(this_response)
