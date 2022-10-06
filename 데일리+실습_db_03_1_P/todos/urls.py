from django.urls import forms
from . import views

app_name="todos"
urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name="create"),
  path('<int:pk>')

]