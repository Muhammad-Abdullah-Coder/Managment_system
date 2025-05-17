from django.db import models
from PIL import Image
from django.utils import timezone

class Student(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    present_percentage = models.FloatField()
    good_work_percentage = models.FloatField()
    joining_month = models.IntegerField()
    joining_year = models.IntegerField()
    image = models.ImageField(upload_to='students/')
    email = models.EmailField()
    number = models.CharField(max_length=15)
    father_number = models.CharField(max_length=15)
    address = models.TextField()
    joining_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 00:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"            