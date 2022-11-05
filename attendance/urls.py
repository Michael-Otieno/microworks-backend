from django.urls import path
from .views import AttendanceList,AttendanceDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
  path('attendance-list',AttendanceList.as_view()),
  path('attendance-list/<str:full_name>',AttendanceDetail.as_view())
]

urlpatterns=format_suffix_patterns(urlpatterns)