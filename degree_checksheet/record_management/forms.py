from django import forms
from checksheet.models import Student

# Student Form

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name"]