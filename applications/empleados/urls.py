from django.urls import path
from . import views

app_name = "empleados_app"

urlpatterns = [
    path('', views.InitialView.as_view()),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name='empleados_all'),
    path(
        'listar-empleados-admin/',
        views.ListEmpleadosAdmin.as_view(),
        name='empleados_admin'),
    path('listar-by-area/<short_name>/',
         views.ListByAreaEmpleado.as_view(), name='empleados_by_departamento'),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view(),),
    path('habilidades/', views.ListHabilidadesEmpleados.as_view()),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='empleado_detalle'),

    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(),
         name='update_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(),
         name='delete_empleado'),
]
