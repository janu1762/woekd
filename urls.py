from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('c1', views.c1, name="c1"),
    path('c2', views.c2, name="c2"),
    path('c3', views.c3, name="c3"),
    path('c4', views.c4, name="c4"),
    path('c5', views.c5, name="c5"),
    path('register', views.register, name="register"),
]
