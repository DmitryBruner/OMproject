from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True,
                                  related_name='posts')  # рекомендуется писать в главном классе а не в обслуживающем это не конвенция а просто мнение  OM

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_absolute_url(
            self):  # создает ссылку на объект тем самым упрощая доступ по соглашениям джанго в разных местах кода
        return reverse('post_detail_url', kwargs={'slug': self.slug})  # функция формирует ссылку на конкретный объект

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})
