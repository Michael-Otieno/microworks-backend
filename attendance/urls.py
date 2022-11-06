from django.urls import path
from .views import AttendanceList,AttendanceDetail
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
  path('attendance-list',AttendanceList.as_view()),
  path('attendance-list/<int:pk>',AttendanceDetail.as_view()),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns=format_suffix_patterns(urlpatterns)