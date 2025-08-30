from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.index, name = "index"),
    path("list/", v.PostListView.as_view(), name="post-list"),
    path("post/<slug:slug>/", v.PostDetailView.as_view(), name="post-detail"),
    path("post/<slug:slug>/like/", v.LikePostView.as_view(), name="post-like"),
]

app_name = "weblog"
