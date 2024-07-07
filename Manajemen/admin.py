from django.contrib import admin
from .models import Siswa, Guru, MataPelajaran

# Register your models here.
admin.site.register(Siswa)
admin.site.register(Guru)
admin.site.register(MataPelajaran)