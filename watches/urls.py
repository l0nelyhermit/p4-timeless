from django.urls import path
from .views import index, create_post, show_post

urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create_post'),
    path('show_post/', show_post, name='show_post'),
]
