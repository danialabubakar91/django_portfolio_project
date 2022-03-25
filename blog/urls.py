from django.urls import path,include
from . import views

urlpatterns = [
    path('hello', views.all_blogs, name='all_blogs')
]