from django import forms
from .models import Course_requirement
from django.forms import FileField
# add crispy form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# validation
from django.core.exceptions import ValidationError

def validate_email(value):
    if value.split("@")[-1].lower() != "email.com":
        raise ValidationError("The email address must end with an @email.com variation")

class ChecklistForm(forms.Form):
    Name = forms.CharField(required=True, min_length=1,max_length=20,widget=forms.EmailInput(attrs={"placeholder": "Your first name and last name"}))
    # email validation
    Email = forms.EmailField(
        required=True, validators=[validate_email], widget=forms.EmailInput(attrs={"placeholder": "Your email address"}))
    Core_Curriculum_Comm_C10_Selection_1 : forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=1), label='Select the first Communication course')
    Core_Curriculum_Comm_C10_Selection_2 : forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=1), label='Select the second Communication course')
    Core_Curriculum_Math_C20 : forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=2), label='Select a Mathematics course')
    Core_Curriculum_Life_and_Physical_Sci_C30_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=5),
        label='Select the first Life and Physical Science course')
    Core_Curriculum_Life_and_Physical_Sci_C30_Selection_2 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=5),
        label='Select the second Life and Physical Science course')
    Core_Curriculum_Lang_Phil_Cult_C40 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=6),
        label='Select a Language, Philosophy and Culture course')
    Core_Curriculum_Creative_Arts_C50 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=7),
        label='Select a Creative Arts course')
    Core_Curriculum_American_Hist_C60_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=8),
        label='Select the first American History course')
    Core_Curriculum_American_Hist_C60_Selection_2 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=8),
        label='Select the second American History course')
    Core_Curriculum_Government_Political_Sci_C70_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=9),
        label='Select the first Government/Political Science course')
    Core_Curriculum_Government_Political_Sci_C70_Selection_2 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=9),
        label='Select the second Government/Political Science course')
    Core_Curriculum_Social_and_Behavioral_Sci_C80 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=3), label='Select a Social and Behavior Science course')
    Core_Curriculum_Component_Area_Option_C90 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=4), label='Select a Component Area Option course')
    University_Core_C80 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    University_Core_C90 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_2 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_3 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_4 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_5 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_6 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_7 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_8 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_9 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_10 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Bachelor_Core_Selection_11 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Department_Core_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Major_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Advanced_Elective_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select a course')
    Advanced_Elective_Selection_1 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select first Elective course')
    Advanced_Elective_Selection_2 = forms.ModelChoiceField(
        queryset=Course_requirement.objects.filter(requirement_id=13), label='Select second Elective course')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.add_input(Submit("", "Submit"))

class UploadForm(forms.Form):
    upload_file = FileField()


