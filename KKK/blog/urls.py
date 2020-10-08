from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', DetailedPost.as_view(), name='post'),
    path('add_post', AddPost.as_view(), name='add_post'),
    path('add_category', AddCategory.as_view(), name='add_category'),
    path('post/update/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('like/<int:pk>', Like, name='like_post'),
    path('category/<str:cats>', Categories, name='categories'),
    path('post/<int:pk>/add_comment', AddComment.as_view(), name='add_comment'),

]
