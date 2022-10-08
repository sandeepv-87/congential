from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        image = request.FILES
        print(image)
    return render(request,'imtopf/index.html')
