
from django.contrib import admin
from django.urls import path
from myapp.views import ati

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads',ati)
]
