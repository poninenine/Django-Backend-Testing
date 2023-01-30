from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('success', views.success, name='success'),
    path('images/', views.display_images, name='display'),
    path('upload/', views.upload_image, name='upload'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('', views.say_hello, name='home'),
]
