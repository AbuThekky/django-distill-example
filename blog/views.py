from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Tag
from django.shortcuts import render
from django.http import HttpResponse
from . import times


def cool_response(request):
    print(times.times)
    return render(request, "base.html", {"time" : times.times})

class IndexView(ListView):

    template_name = 'index.html'
    model = Post
    allow_empty = False
    queryset = Post.objects.published()
    ordering = '-created'
    context_object_name = 'posts'


class PostView(DetailView):

    template_name = 'post.html'
    model = Post


class TagView(DetailView):

    template_name = 'tag.html'
    model = Tag
    slug_url_kwarg = 'tag'
    slug_field = 'name'

