from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, DashboardView, StudentDetailView
from .views import AddStudentView, MarkAttendanceView, AttendanceListView, TotalStudentView,  DeleteStudentView, UserSettingsView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('add_student/', AddStudentView.as_view(), name='add_student'),
    path('mark-attendance/', MarkAttendanceView.as_view(), name='mark_attendance'),
    path('attendance-list/', AttendanceListView.as_view(), name='attendance_list'),
    path('total-students/', TotalStudentView.as_view(), name='total_students'),
    path('student/<int:pk>/delete/', DeleteStudentView.as_view(), name='delete_student'),
    path('settings/', UserSettingsView.as_view(), name='settings'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
