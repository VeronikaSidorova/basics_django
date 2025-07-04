from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("create/", BlogCreateView.as_view(), name="post_create"),
    path("post/update/<int:pk>/", BlogUpdateView.as_view(), name="post_update"),
    path("post/delete/<int:pk>/", BlogDeleteView.as_view(), name="post_delete"),
]
