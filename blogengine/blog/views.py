from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .forms import *
from .models import *
from .utils import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDatailMixin,
                 View):  # порядок наследования важен! сначала ищется в первом классе и если не находит то во втором. для вывода иерархии обратиться к методу класса mro()
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'


class TagDetail(ObjectDatailMixin, View):
    model = Tag
    template = 'blog/list_posts_tag.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'
