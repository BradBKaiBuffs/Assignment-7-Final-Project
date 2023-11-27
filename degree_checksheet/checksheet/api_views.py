# rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course

@api_view()
def course_api_view(request):
    num_courses = Course.objects.count()
    return Response({"num_courses":num_courses})