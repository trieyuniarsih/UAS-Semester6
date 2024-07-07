from rest_framework import serializers
from .models import Siswa, Guru, MataPelajaran

class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = '__all__'

class GuruSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guru
        fields = '__all__'

class MataPelajaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataPelajaran
        fields = '__all__'
