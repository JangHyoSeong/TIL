from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='home'),
    path('community/', views.community, name='community'),
]
