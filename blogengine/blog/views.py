from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import *
from .utils import *


def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    context = {'page_obj': page,
               'is_paginated': is_paginated,
               'prev_url': prev_url,
               'next_url': next_url}
    return render(request, 'blog/index.html', context=context)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin,
                 View):  # порядок наследования важен! сначала ищется в первом классе и если не находит то во втором. для вывода иерархии обратиться к методу класса mro()
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_template = 'posts_list_url'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/list_posts_tag.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_template = 'tags_list_url'
    raise_exception = True
