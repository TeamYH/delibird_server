from django.urls import path
from superuser_db import views


urlpatterns = [
    path('counsel_list', views.counsel_manager),
]

