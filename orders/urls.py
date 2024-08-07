from django.urls import path
from . import views
urlpatterns = [
    path('createOrder/',views.createOrder),
    path('getOrderByEmail/<str:email>',views.getOrderByEmail),
    path('getAllOrders/',views.getAllOrders),
    path('updateorder/', views.update_order),
]
