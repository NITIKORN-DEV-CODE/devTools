from django.urls import path
from province import views

urlpatterns = [
    path('province', views.provinceApi_province),
    path('province/<int:pk>', views.provinceApi_province),
    path('province/amphoe', views.provinceApi_amphoeprovince),
    path('province/amphoe/<int:pk>', views.provinceApi_amphoeprovince),
    path('province/tambol', views.provinceApi_tambolamphoe),
    path('province/tambol/<int:pk>', views.provinceApi_tambolamphoe),
    path('amphoe', views.provinceApi_amphoe),
    path('amphoe/<int:pk>', views.provinceApi_amphoe),
    path('tambol', views.provinceApi_tambol),
    path('tambol/<int:pk>', views.provinceApi_tambol),
    ]
