from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *


# в миксинах мы создаем переменные для тех кусков кода которые индивидуальны. и дальше прописываем общую логику программы
class ObjectDatailMixin():
    model = None
    template = None
    def get(self, request, slug):
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object}) #тут мы через нейм обращаемся к имени модели (строка) и после делаем все буквы строчными
