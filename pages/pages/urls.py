from django.contrib import admin
from django.urls import path

from main_pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
]
