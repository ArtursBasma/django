from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),  # Šeit ir izmantots pareizais funkcijas nosaukums
    path('ff', views.home, name='home'),
    path('cheatsheet', views.cheatsheet, name='cheatsheet'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]
