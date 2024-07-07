from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Siswa, Guru, MataPelajaran
from .serializers import SiswaSerializer, GuruSerializer, MataPelajaranSerializer

# view untuk sekolah dengan class base view
class SiswaList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        siswa = Siswa.objects.all()
        serializer = SiswaSerializer(siswa, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiswaDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Siswa.objects.get(pk=pk)
        except Siswa.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        siswa = self.get_object(pk)
        serializer = SiswaSerializer(siswa)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        siswa = self.get_object(pk)
        serializer = SiswaSerializer(siswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        siswa = self.get_object(pk=pk)
        siswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# view untuk siswa dengan class base view
class GuruList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        guru = Guru.objects.all()
        serializer = GuruSerializer(guru, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GuruSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuruDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Guru.objects.get(pk=pk)
        except Guru.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        guru = self.get_object(pk)
        serializer = GuruSerializer(guru)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        guru = self.get_object(pk)
        serializer = GuruSerializer(guru, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        guru = self.get_object(pk=pk)
        guru.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# view untuk pendaftaran dengan class base view
class MataPelajaranList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        matapelajaran = MataPelajaran.objects.all()
        serializer = MataPelajaranSerializer(matapelajaran, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MataPelajaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MataPelajaranDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return MataPelajaran.objects.get(pk=pk)
        except MataPelajaran.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        matapelajaran = self.get_object(pk)
        serializer = MataPelajaranSerializer(matapelajaran)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        matapelajaran = self.get_object(pk)
        serializer = MataPelajaranSerializer(matapelajaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        matapelajaran = self.get_object(pk=pk)
        matapelajaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)