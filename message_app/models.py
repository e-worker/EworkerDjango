from django.db import models
from datetime import datetime
from employer.models import Company
from student.models import Student
# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key = True)
    header = models.CharField(max_length=50)
    content = models.CharField(max_length=512)
    creation_date = models.DateTimeField(default=datetime.now)
    student = models.ForeignKey('student.Student', models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    def __str__(self):
        return str(self.header)