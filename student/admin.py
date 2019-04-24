from django.contrib import admin
from .models import Student, StudentDegreeCourse, StudentInfo, StudentLanguage, StudentSkill

admin.site.register(Student)
admin.site.register(StudentDegreeCourse)
admin.site.register(StudentInfo)
admin.site.register(StudentLanguage)
admin.site.register(StudentSkill)



