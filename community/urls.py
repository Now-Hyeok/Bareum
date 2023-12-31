from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CommentListView

urlpatterns = [

    path('list/', views.PostListView.as_view(), name='post-list'),
    path('newslist/',views.NewsListView.as_view(), name='news-list'),
    path('like_post', views.like_post),
    path('write',views.write_post),
    path('detail/<int:post_id>',views.post_detail),
    path('popularlist', views.popular_posts, name='popular_posts'),
    path('comments/<int:post_id>', views.CommentListView.as_view(), name='comments_list'),
    path('comments/reply/<int:comments_id>',views.CommentReplyListView.as_view(), name='comments_reply_list'),
    path('detail/<int:post_id>/', views.delete_post, name='delete-post'),
    path('update/<int:post_id>', views.update_post, name='update_post'),
    path('posts/comments/delete/<int:comments_id>', views.CommentReplyListView.as_view(), name='comment-delete'),

]


