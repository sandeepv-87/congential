from django.shortcuts import render, HttpResponse, redirect ,HttpResponseRedirect
from PIL import Image
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import img2pdf
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import user_pdf, testing
import os


# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        pdfs = user_pdf.objects.filter(user=user)
        return render(request, 'imtopf/dashboard.html', {'pdfs': pdfs,'show':True})
    else:
        return redirect('login')


def index(request):
    user = request.user
    if request.method == 'POST':
        images = request.FILES.getlist('image')
        pdfs = []
        for img in images:
            img_name = img.name
            imgObj = Image.open(img)
            img_name = img_name.split('.')[0]
            imgObj.save(f'{img_name}.pdf')
            pdf = open(f'{img_name}.pdf', 'rb')
            pdf_file = File(pdf)
            if not user.is_authenticated:
                user = None
            current_pdf = user_pdf(image_name=img_name, user=user, user_image=img, user_pdf=pdf_file)
            current_pdf.save()
            pdfs.append(current_pdf)
            pdf.close()
            os.remove(f'{img_name}.pdf')
        return render(request, 'imtopf/index.html', {'pdfs': pdfs, 'user': user,'show':True})
    else:
        return render(request, 'imtopf/index.html', {'user': user,'show':True})


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'imtopf/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Failed to Authenticate Check credentials')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'imtopf/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request,'imtopf/pdfhome.html')