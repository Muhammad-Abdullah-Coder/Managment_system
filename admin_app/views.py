from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Attendance, Student
from .forms import AttendanceForm, StudentForm, UserSettingsForm
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('dashboard')

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have successfully logged out.')
        return super().dispatch(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'dashboard.html'
    context_object_name = 'students'
    login_url = 'login'

    def get_queryset(self):
        return Student.objects.all()

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
    login_url = 'login'

class AddStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('dashboard')
    login_url = 'login'

class MarkAttendanceView(FormView):
    template_name = 'mark_attendance.html'
    form_class = AttendanceForm
    success_url = reverse_lazy('attendance_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        context['attendance_list'] = Attendance.objects.all()
        return context

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list.html'
    context_object_name = 'attendances'        

class TotalStudentView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'total_student.html'
    context_object_name = 'students' 
    login_url = 'login'

class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('dashboard') 

class UserSettingsView(FormView):
    template_name = 'settings.html'
    form_class = UserSettingsForm 
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Settings updated successfully!')
        return super().form_valid(form)