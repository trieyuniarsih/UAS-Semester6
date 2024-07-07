from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('siswa/', views.SiswaList.as_view()),
    path('siswa/<int:pk>/', views.SiswaDetail.as_view()),
    path('guru/', views.GuruList.as_view()),
    path('guru/<int:pk>/', views.GuruDetail.as_view()),
    path('matapelajaran/', views.MataPelajaranList.as_view()),
    path('matapelajaran/<int:pk>/', views.MataPelajaranDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)