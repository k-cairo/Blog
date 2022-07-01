from django.urls import path
from .views import index, new_post, post, edit_post, delete_post, about

urlpatterns = [
    path('', index, name='blog-index'),
    path('post/<slug:slug>/', post, name='blog-post'),
    path('new_post/', new_post, name='blog-new_post'),
    path('edit-post/<slug:slug>/', edit_post, name='blog-edit_post'),
    path('delete/<slug:slug>/', delete_post, name='blog-delete_post'),
    path('about/', about, name='blog-about'),
    ]
