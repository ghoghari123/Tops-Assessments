
from django.urls import path
from .views import *

urlpatterns = [
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
    path('comment/<int:post_id>/', add_comment, name='add_comment'),
    path('delete-comment/<int:id>/', delete_comment, name='delete_comment'),
    path('follow/<int:user_id>/', toggle_follow, name='toggle_follow'),
]
