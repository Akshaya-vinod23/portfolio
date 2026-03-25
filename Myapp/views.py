from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse
import os

def home(request):
    return render(request, 'index.html')

def download_cv(request):
    file_path = os.path.join(settings.BASE_DIR, 'Myapp/static/files/cv.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True)

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, email, message)  # for testing

    return render(request, 'contact.html')

def skills(request):
    return render(request, 'skills.html')
