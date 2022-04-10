from django.urls import path

from . import views


app_name="resumeranker"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.send_files, name="uploads"),
    path('keywords/', views.send_keywords, name="keywords"),
    path('reset/', views.reset, name="reset")
]