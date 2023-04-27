from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *


# в миксинах мы создаем переменные для тех кусков кода которые индивидуальны. и дальше прописываем общую логику программы
class ObjectDatailMixin():
    model = None
    template = None
    def get(self, request, slug):
        object = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): object}) #тут мы через нейм обращаемся к имени модели (строка) и после делаем все буквы строчными

class ObjectCreateMixin():
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        else:
            return render(request, self.template, context={'form': bound_form})

