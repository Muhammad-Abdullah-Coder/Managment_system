from django import forms
from .models import Student, Attendance
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'occupation', 'present_percentage', 'good_work_percentage', 'joining_month', 'joining_year', 'image', 'email', 'number', 'father_number', 'address']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'status']        

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(UserSettingsForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = user.username
        self.fields['email'].initial = user.email