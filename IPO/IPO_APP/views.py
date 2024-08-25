from django.shortcuts import render

# Create your views here.

def UpcomingIPO(request):
    return render(request,'UpcomingIPO.html')

def  broker(request):
    return render(request,'broker.html')