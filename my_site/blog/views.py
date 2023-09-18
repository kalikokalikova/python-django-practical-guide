from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from .models import Post

def get_date(post):
  return post['date']

def index(request):
  latest_posts = Post.objects.all().order_by("-date")[:3]
  return render(request, "blog/index.html", {
    "posts": latest_posts
  })

def posts(request):
  all_posts = Post.objects.all().order_by("-date")
  return render(request, "blog/posts.html", {
    "posts": all_posts
  })

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, "blog/post.html", {
    "post": post,
    "tags": post.tags.all()
  })