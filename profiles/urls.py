from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile_view, name='profile'),
]