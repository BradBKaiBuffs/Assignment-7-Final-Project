from django.urls import path
from .views import StudentRecordView, FormSuccessView

urlpatterns = [
    # for class base view "Student Form"
    path('new_student_record', StudentRecordView.as_view(), name='student_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
]