from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.models import Document
from uploads.forms import DocumentForm


def home_(request):
    documents = Document.objects.all()
    return render(request, 'templates/home.html', { 'documents': documents })


def upload_simple(request):
    print("in upload\n")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'uploads/upload.html')


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            filename = form.save()
            uploaded_file_url = filename.description
        return render(request, 'uploads/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    else:
        form = DocumentForm()
    return render(request, 'uploads/upload.html', {
        'form': form
    })
