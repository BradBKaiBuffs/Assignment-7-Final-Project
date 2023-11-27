from django.db import models

# Create your models here.

# CHOICE OF YES OR NO
class Choice(models.TextChoices):
    Yes = "YES", "Yes"
    No = "NO", "No"

# Create your models here.
# Student
class Student (models.Model):
    wt_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)

    def __str__(self):
        # return f"Student ID: {self.wt_id}, Student Name: {self.first_name} {self.last_name}"
        return f"{self.wt_id}"

# Course
class Course (models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 20)
    course_title = models.CharField(max_length = 60)
    course_desc = models.CharField(max_length = 60, default='None')
    credit_hours = models.IntegerField(default=3)
    prerequisite = models.BooleanField(default=False)
    semester = models.CharField(max_length = 10, default='TBD')

    def __str__(self):
        # return f"Course ID: {self.course_id}, Course Name: {self.course_name}, Course Title:{self.course_title}, Credit Hours: {self.credit_hours}, Semester {self.semester}"
        # return name instead of ID since it is more readable for this stage
        return self.course_name

# Major
class Major (models.Model):
    major_id = models.AutoField(primary_key = True)
    major_name = models.CharField(max_length = 60)
    total_hours = models.IntegerField()

    def __str__(self):
        # return f"Major ID: {self.major_id}, Major Name: {self.major_name}, Total Hours: {self.total_hours}"
        # return name instead of ID since it is more readable for this stage
        return self.major_name

# Requirement
class Requirement (models.Model):
    requirement_id = models.AutoField(primary_key = True)
    req_type = models.CharField(max_length = 60)
    req_desc = models.CharField(max_length = 60)
    req_hours = models.IntegerField()

    def __str__(self):
        # return f"Req. ID: {self.requirement_id}, Req. Type: {self.req_type}, Req. Desc.: ({self.req_desc}) Req. Hours: {self.req_hours}"
        return f"{self.requirement_id}"

# Enroll
class Enroll (models.Model):
    enroll_id = models.AutoField(primary_key = True)
    wt_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # return f"Enroll ID: {self.enroll_id}, WT ID: {self.wt_id}, Course ID: {self.course_id}, Enroll Date: {self.enroll_date}"
        return f"{self.enroll_id}"

# Major_requirement
class Major_requirement (models.Model):
    majorreq_id = models.AutoField(primary_key = True)
    major_id = models.ForeignKey(Major, on_delete = models.CASCADE)
    requirement_id = models.ForeignKey(Requirement, on_delete = models.CASCADE)

    def __str__(self):
        # return f"Major Req. ID: {self.maj_req_id}, Major ID: {self.major_id}, Requirement ID: {self.requirement_id}"
        return f"{self.majorreq_id}"

# Major_selection
class Major_selection (models.Model):
    majorsel_id = models.AutoField(primary_key = True)
    wt_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    major_id = models.ForeignKey(Major, on_delete = models.CASCADE)
    selection_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        # return f"Major Selection ID: {self.maj_sel_id}, WT ID: {self.wt_id}, Major ID: {self.major_id}, Selection Date: {self.selection_date}"
        return f"{self.majorsel_id}"

# Course_requirement
class Course_requirement (models.Model):
    coursereq_id = models.AutoField(primary_key = True)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
    requirement_id = models.ForeignKey(Requirement, on_delete = models.CASCADE)
    recommended = models.CharField(max_length= 3, choices=Choice.choices)
    lang_equiv = models.CharField(max_length = 3, choices=Choice.choices)

    def __str__(self):
        # return f"Course Req. ID: {self.course_req_id}, Course ID: {self.course_id}, Requirement ID: {self.requirement_id}, Recommended?: {self.recommended}, Language Equivalent?: {self.lang_equiv}"
        return f"{self.course_id}"