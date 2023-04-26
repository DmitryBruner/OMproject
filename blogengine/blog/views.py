from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import *
from .utils import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDatailMixin, View): # порядок наследования важен! сначала ищется в первом классе и если не находит то во втором. для вывода иерархии обратиться к методу класса mro()
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDatailMixin, View):
    model = Tag
    template = 'blog/list_posts_tag.html'
