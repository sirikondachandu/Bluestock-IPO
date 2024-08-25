from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpcomingIPO, name="UpcomingIPO"),
    path('broker/', views.broker, name="broker"),
    path('all_brokers/', views.all_brokers, name="all_brokers"),
    path('community/', views.community, name="community"),
    path('shark_investors/', views.shark_investors, name="shark_investors"),
    path('shark_school/', views.shark_school, name="shark_school"),
    path('technical/', views.technical, name="technical"),
    path('signIn/', views.signIn, name="signIn"),
    path('signUp/', views.signUp, name="signUp"),
    path('forget/', views.forget, name="forget"),
]
