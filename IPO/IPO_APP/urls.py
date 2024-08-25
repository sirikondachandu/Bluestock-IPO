from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpcomingIPO, name="UpcomingIPO"),
    path('broker/', views.broker, name="broker"),
]
