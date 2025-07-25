from django.urls import path

from . import views

urlpatterns = [
    path("list_post/", views.ListPostAPIView.as_view(), name="list-posts"),
    path("post/<int:pk>/", views.PostDetailsView.as_view(), name="post-detail"),
]
