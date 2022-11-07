from django.shortcuts import render
from .serializers import AttendanceListSerializer
from rest_framework import generics
from .models import Attendance
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Q
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from attendance.pagination import CustomPageNumberPagination
# Create your views here.

class AttendanceList(generics.GenericAPIView):
  """
  List of all attendance
  """
  pagination_class=CustomPageNumberPagination
  serializer_class=AttendanceListSerializer
  pagination_class.page_size=1
  def get_queryset(self):
    return Attendance.objects.all()

  def get(self,request,format=None):
    query=request.GET.get('query')

    if query==None:
      query=""
      # http://127.0.0.1:8000/attendance-list?query=jj@gmail.com
    attendance=Attendance.objects.filter(Q(full_name__icontains=query) | Q(email__icontains=query)) 
    serializer=AttendanceListSerializer(attendance,many=True)
    return Response(serializer.data)

  def post(self,request,format=None):
    serializer=AttendanceListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AttendanceDetail(generics.GenericAPIView):
  """
  Retrieve, update or delete someone's attendance details
  """
  permission_classes = [IsAuthenticated]

  serializer_class=AttendanceListSerializer
  def get_object(self, pk):
    try:
      return Attendance.objects.get(pk=pk)
    except Attendance.DoesNotExist:
      raise Http404

  def get(self,request,pk,format=None):
    # attendance=self.get_object(full_name)
    attendance=Attendance.objects.get(pk=pk)
    serializer=AttendanceListSerializer(attendance)
    return Response(serializer.data)

  def put(self,request,pk,format=None):
    attendance=self.get_object(pk)
    serializer=AttendanceListSerializer(attendance,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

  def delete(self,request,pk,format=None):
    attendance=self.get_object(pk)
    attendance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


