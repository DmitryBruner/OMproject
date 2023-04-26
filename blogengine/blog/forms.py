from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_slug(self):
        new_slug = self.cleaned_data[
            'slug'].lower()  # это антипаттерн тк нужно обращаться через гет но в данном случае запись корректна тк значение точно будет в бд
        if new_slug == 'create':
            raise ValidationError('Slug are not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be unique. We have "{new_slug}" slug already')

        return new_slug

    def save(self):
        new_tag = Tag.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug']
        )
        return new_tag
