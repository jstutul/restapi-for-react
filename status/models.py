from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    city=models.CharField(max_length=30,blank=False)
    phone=models.IntegerField()
    images=models.ImageField(upload_to="student/",default="default.jpg")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Student List"
        ordering=["-id"]