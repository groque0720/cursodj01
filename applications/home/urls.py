
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('vista/', views.PruebaListView.as_view()),
    path('vista-prueba/', views.ModeloPruebaListView.as_view()),
    path('add-prueba/', views.PruebaCreateView.as_view(), name='prueba_add'),
]
