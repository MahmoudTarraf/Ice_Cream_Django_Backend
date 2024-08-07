from django.urls import path
from . import views

urlpatterns = [
    path('createoffer/',views.create_offer),
    path('getalloffers/',views.get_all_offers),
    path('deleteoffer/', views.delete_offer),
    path('searchoffer/', views.search_offer),
]
