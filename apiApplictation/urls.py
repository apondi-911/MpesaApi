from django.urls import path, include
from django_daraja import mpesa, urls

from . import views
from .views import mpesa_callback

urlpatterns = [
    path('', views.index, name='index-url'),
    path('mpesa-callback/', mpesa_callback, name='mpesa-callback')

]
