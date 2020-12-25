from django.urls import path

from . import views

urlpatterns = [
  path('', views.app1_view, name='app1_view'),
  ]
