from django.contrib import admin
# import models for admin
from checksheet.models import(Student, Course, Major, Requirement, Enroll, Major_requirement, Major_selection, Course_requirement)

# Register your models here.
# Register models for admin
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Major)
admin.site.register(Requirement)
admin.site.register(Enroll)
admin.site.register(Major_requirement)
admin.site.register(Major_selection)
admin.site.register(Course_requirement)
