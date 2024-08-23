from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('IPO_APP/', include('IPO_APP.urls')),
]
