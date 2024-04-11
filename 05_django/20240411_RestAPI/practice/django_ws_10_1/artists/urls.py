from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.create_artist),
]
