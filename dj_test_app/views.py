from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from DjangoTesting import settings
from .forms import ImageForm
import os


# Create your views here.
def say_hello(request):
    return render(request, 'hello.html')

def success(request):
    return render(request, 'success.html')

def display_images(request):
 
    if request.method == 'GET':
 
        Images = Image.objects.all()
        return render(request, 'images.html', {'image_list': Images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('display')