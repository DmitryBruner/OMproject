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


class TagDetail(ObjectDatailMixin, View):
    model = Tag
    template = 'blog/list_posts_tag.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    #
    # def get(self, request):
    #     form = TagForm
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     else:
    #         return render(request, 'blog/tag_create.html', context={'form': bound_form})
    #

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'