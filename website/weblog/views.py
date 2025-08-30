from asyncio import run
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import JsonResponse
from .models import Post, Like
from .forms import CommentForm


def index(request):
    template_name = "weblog/index.html"
    response = render(request, template_name)
    return response


class PostListView(ListView):
    model = Post
    template_name = "weblog/post/list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "weblog/post/detail.html"
    context_object_name = "post"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comments.all()
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect("weblog:post-detail", slug=self.object.slug)
        return self.render_to_response({"form": form})


class LikePostView(View):


    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        try:
            like = Like.objects.get(user = request.user, post = post)
            liked = True
        except:
            liked = False
        response = {
            "liked": liked
        }
        response = JsonResponse(response)
        return response
    

    def post(self, request, slug):
        post = Post.objects.get(slug = slug)
        like, created = Like.objects.get_or_create(user = request.user, post = post)
        result = {
            "liked": created
        }
        if not created:
            self.delete(request, slug)
        response = JsonResponse(result)
        return response


    def delete(self, request, slug):
        post = Post.objects.get(slug = slug)
        like = Like.objects.filter(user = request.user, post=post)
        like.delete()
