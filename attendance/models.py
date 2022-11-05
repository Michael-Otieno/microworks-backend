from django.db import models

# Create your models here.

class Attendance(models.Model):
  full_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255,unique=True)
  machine_id = models.CharField(max_length=255,null=True)
  availability = models.TextField()
  time_in = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['full_name']

  def __str__(self):
        return self.full_name
