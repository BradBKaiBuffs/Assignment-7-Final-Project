from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import StudentForm
from django.views import View
# Class based view login required import
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Student Record Class View

class StudentRecordView(LoginRequiredMixin, FormView):
    template_name = 'student_form.html'
    form_class = StudentForm
    success_url = '/record_management/entry_success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Record saved")