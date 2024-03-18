from django.http import HttpResponse
from django.shortcuts import render

# from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm

from applications.empleados.models import Empleado
from applications.departamentos.models import Departamento


class NewDepartamentoView(FormView):
    template_name = 'departamentos/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form) -> HttpResponse:

        dpto = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
        dpto.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job=1,
            departamento=dpto
        )
        return super(NewDepartamentoView, self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamentos/lista-departamento.html"
    context_object_name = 'departamentos'
