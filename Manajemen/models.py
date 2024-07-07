from django.db import models

# Create your models here.
class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    kelas = models.CharField(max_length=50)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Guru(models.Model):
    nama = models.CharField(max_length=255)
    bidang = models.CharField(max_length=255)
    telepon = models.CharField(max_length=20)

    def __str__(self):
        return self.nama

class MataPelajaran(models.Model):
    nama = models.CharField(max_length=255)
    guru = models.ForeignKey('Guru', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama