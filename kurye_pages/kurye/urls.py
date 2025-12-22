from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kurye_pages.urls')),   # tüm siteyi app’e yönlendir
]
