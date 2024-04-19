from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/comments_create/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
