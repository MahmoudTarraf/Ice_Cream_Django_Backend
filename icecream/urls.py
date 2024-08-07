from django.urls import path
from . import views
urlpatterns = [
    path('createicecream/',views.create_icecream),
    path('geticecreams/',views.get_all_icecream),
    path('updateicecream/<int:ice_cream_id>/', views.update_ice_cream),
    path('deleteicecream/', views.delete_ice_cream),
     path('searchicecream/', views.search_ice_cream),
    path('',views.welcome),
]
