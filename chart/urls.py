# chart\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('covid19new/', views.home, name='home'),
]
