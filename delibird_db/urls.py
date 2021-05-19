from django.urls import path
from delibird_db import views


urlpatterns = [
    path('table_list', views.table_manager),
]

