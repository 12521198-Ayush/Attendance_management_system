from django.urls import path
from attendance_app.views import *
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/student/', StudentCreateView.as_view(), name='student_detail'),
    path('api/attendance/', StudentDetailView.as_view(), name='attendance_create'),
    path('api/update_attendance/', AttendanceUpdateView.as_view(), name='attendance_update'),
    path('api/update_password/', ChangePasswordView.as_view(), name='password_update'),
    path('api/delete_student/', StudentDeleteView.as_view(), name='delete_student'),



    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/all_student/', StudentListView.as_view(), name='students'),
    path('api/delete_all/', StudentDeleteAllView.as_view(), name='delete'),

    path('admin/', admin.site.urls),

]
