from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'app1/app1.html')

def index(request):
    return render(request,'app1/app2.html')
