from django.urls import path

from . import views

app_name = 'repair'

urlpatterns = [
    path('', views.index, name='index'),
]