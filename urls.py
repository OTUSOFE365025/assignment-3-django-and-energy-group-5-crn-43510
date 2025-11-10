from django.contrib import admin
from django.urls import path
from register import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.scan_view, name="scan"), 
]
