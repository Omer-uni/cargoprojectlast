from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),              
    path('accounts/', include('accounts.urls')),
    path('', include('cargoposts.urls')),      
    path('dashboard/', include('management.urls')),
    path('admin/', admin.site.urls),
]
