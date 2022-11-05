from .models import Attendance
from rest_framework import serializers

class AttendanceListSerializer(serializers.ModelSerializer):

  class Meta:
    model=Attendance
    fields=['id','full_name','email','machine_id','availability','time_in']