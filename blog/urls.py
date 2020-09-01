from django.urls import path
from .views import (
 PostListView,
 PostDetailView,
 PostCreateView,
 PostUpdateView,
 PostDeleteView,
 UserPostListView
)
from  . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'), # we can see the posts based on the user primary key
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.about,name='blog-about'),
]


#<app>/<model>_<viewtype>.html -- blog/post_list.html

