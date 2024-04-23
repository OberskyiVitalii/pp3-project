from django.urls import path

from . import views

app_name = 'repair'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('<int:service_id>/', views.detail_service, name='detail_service'),
    path('order-service/', views.order_service, name='order_service'),
    path('profile/', views.profile, name='profile'),
    path('add-device/', views.add_device, name='add_device'),
    path('<int:device_id>/delete-device/', views.delete_device, name='delete_device'),
    path('<int:device_id>/edit-device/', views.edit_device, name='edit_device'),
    path('create-service/', views.create_service, name='create_service'),
    path('<int:service_id>/delete-service/', views.delete_service, name='delete_service'),
    path('<int:service_id>/edit-service/', views.edit_service, name='edit_service'),
    path('create-service-center/', views.create_service_center, name='create_service_center'),
    path('delete-service-center/<int:service_center_id>/', views.delete_service_center, name='delete_service_center'),
    path('edit-service-center/<int:service_center_id>/', views.edit_service_center, name='edit_service_center'),
]