from django.urls import path
from .views import *

urlpatterns = [

    # LIKE
    path('like/<int:id>/', like_post, name='like_post'),

    # COMMENT
    path('comment/add/<int:id>/', add_comment, name='add_comment'),
    path('comment/edit/<int:id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:id>/', delete_comment, name='delete_comment'),

    # FOLLOW
    path('follow/<int:id>/', follow_user, name='follow_user'),
]