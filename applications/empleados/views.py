from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)

from .models import Empleado
from .forms import EmpleadoForm


class InitialView(TemplateView):
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self) -> QuerySet[Any]:
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListByAreaEmpleado(ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self) -> QuerySet[Any]:
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            departamento__name=area
        )
        return lista


# class ListByAreaEmpleado(ListView):
#     template_name = 'empleados/list_by_area.html'

#     def get_queryset(self) -> QuerySet[Any]:
#         area = self.kwargs['short_name']
#         lista = Empleado.objects.filter(
#             departamento__name=area
#         )
#         return lista


class ListEmpleadosByKword(ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self) -> QuerySet[Any]:
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista


class ListHabilidadesEmpleados(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self) -> QuerySet[Any]:
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detalle_empleado.html"
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        empleado = self.object  # Acceder al objeto Empleado actual
        context['habilidades'] = empleado.habilidades.all()
        return context


class SuccessView(TemplateView):
    template_name = "empleados/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleados/add.html"
    form_class = EmpleadoForm
    # fields = ['first_name', 'last_name', 'job',
    #           'departamento', 'habilidades', 'avatar']
    success_url = reverse_lazy('empleados_app:empleados_all')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleados/update.html"
    fields = ['first_name', 'last_name', 'job',
              'departamento', 'habilidades', 'avatar']
    success_url = reverse_lazy('empleados_app:empleados_all')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleados_app:empleados_all')
    context_object_name = 'empleado'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class ListEmpleadosAdmin(ListView):
    template_name = 'empleados/list_empleados.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
