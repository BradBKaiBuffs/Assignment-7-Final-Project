from django.contrib import admin
# import for upload
from checksheet.models import Course
from django.shortcuts import render
from django.urls import path
from checksheet.forms import UploadForm
from django.conf import settings
import csv


# Register your models here.
# custom admin branding
class ChecksheetAdmin(admin.AdminSite):
    site_header = "Checklist Administration"
    logout_template = "admin/logout.html"

# upload function
    def upload_csv(self,request):
        if request.method == "POST":
            form = UploadForm(request.POST, request.FILES)

            if form.is_valid():
                save_path = settings.MEDIA_ROOT / form.cleaned_data["upload_file"].name

                with open(save_path, "wb") as output_file:
                    for chunk in form.cleaned_data["upload_file"].chunks():
                        output_file.write(chunk)

                # reads csv test_file1.csv and inserts into Course table according to order of csv file
                with open(save_path, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    next(reader, None)
                    for item in reader:
                        Course.objects.create(
                            course_name=item[0],
                            course_title=item[2],
                            course_desc=item[3]
                        )

        else:
            form = UploadForm()
        return render(request, "admin/upload.html", {"form": form})

# creates customization of page for upload
    def get_urls(self):
        urls = super().get_urls()
        urlpatterns = [path("upload/", self.upload_csv)]
        return urlpatterns + urls
