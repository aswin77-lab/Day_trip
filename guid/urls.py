from django.urls import path
from . import views

urlpatterns = [
    path('', views.guid_home, name='guid_home'),
]