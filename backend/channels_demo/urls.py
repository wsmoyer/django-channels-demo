from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    path('dashboard/', include('apps.chan.urls')),
]
