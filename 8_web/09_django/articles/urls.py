from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    path('', views.index, name="index"), #뒤에 아무것도 안붙으면 views.index로
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    # --------------------------------------------------
    path('main/', views.main, name= 'main'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name= 'detail'),

    #수정
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    
]