from django.shortcuts import render, get_object_or_404, redirect
from .forms import ChecklistForm
# login requirement
from django.contrib.auth.decorators import login_required
# import for csv generation
import csv
# import for pdf generation
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
# upload form
from .forms import UploadForm



# Create your views here.
def index (request):
    return render(request, "base.html")

# add a home page
def home(request):
    return render(request, "home.html",{})

# Degree courses selection form
@login_required
def checklist(request):
    mylist = []
    if request.method == "POST":
        form = ChecklistForm(request.POST)
        if form.is_valid():
            # creates a list of form selections
            for name, value in form.cleaned_data.items():
                mylist.append("{}: {}".format(name, value))
            print(mylist)
            # pdf creation
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename="checklist_pdf.pdf"'
            p = canvas.Canvas(response)
            # for loop to iterate through lines for pdf
            for i, line in enumerate (mylist):
                p.drawString(1 * cm, 29.7 * cm - 1 * cm - i * cm, line)
            p.save()
            # csv export of course selection
            header = ['Degree selection']
            filename = 'degree_checklist.csv'
            try:
                with open(filename, 'w') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(header)
                    for item in mylist:
                        csv_writer.writerow([item])
            except (IOError, OSError) as csv_file_error:
                print("Unable to write the contents to csv file. Exception: {}".format(csv_file_error))
            return response
    else:
        form = ChecklistForm()
    return render(request, 'checklist.html', {'method':request.method, "form":form})

# profile
def profile(request):
    return render(request, 'profile.html')

# File upload
@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            save_path = settings.MEDIA_ROOT / form.cleaned_data["upload_file"].name

            with open(save_path, "wb") as output_file:
                for chunk in form.cleaned_data["upload_file"].chunks():
                    output_file.write(chunk)

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

    return render(request, "upload.html",{"form":form})
