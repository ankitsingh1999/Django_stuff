from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    stu_id = models.IntegerField()
    stu_name = models.CharField(max_length=16)
    stu_email = models.EmailField(max_length=20)
    stu_pass = models.CharField(max_length=20)

# def __repr__(self):
#     return self.stu_name


class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=25)

























''' 
Commands - Makemigrations, migrate
python manage.py sqlmigrate app_name migration_file_name
python manage.py showmigration
'''

