from django.shortcuts import render, HttpResponse
from PIL import Image
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import img2pdf


# Create your views here.
def index(request):
    if request.method == 'POST':
        image = request.FILES['image']
        image_name = image.__str__()
        imgObj = Image.open(image)
        imgObj.show()

        return HttpResponse('Image uploaded')
    return render(request, 'imtopf/index.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('User created')
    else:
        return render(request, 'imtopf/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('User logged in')
        else:
            return HttpResponse('User not logged in')
    else:
        return render(request, 'imtopf/login.html')


def user_logout(request):
    logout(request)
    return HttpResponse('User logged out')
