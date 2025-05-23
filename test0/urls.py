from django.contrib import admin
from django.urls import path,include
from test0.views import upload_image,result_image
from . import views
urlpatterns = [
     path('', views.index, name = 'index'),
     path('herbal', views.Herbal, name = 'herbal'),
     path("t1",upload_image,name = 't1'),
     path("t1_result",result_image , name = 't1_result'),
     path('skincare', views.skincare, name = 'skincare'),
     path('dry', views.dry, name = 'dry'),
     path('mix', views.mix, name = 'mix'),
     path('normal', views.norm, name = 'normal'),
     path('oily', views.oily, name = 'oily')
]
