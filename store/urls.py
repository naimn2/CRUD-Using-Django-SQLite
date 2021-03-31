from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('hapus/', views.hapus),
    path('ubah/', views.ubah),
    path('ubah/simpan/', views.simpan),
    path('tambah/', views.tambah)
]