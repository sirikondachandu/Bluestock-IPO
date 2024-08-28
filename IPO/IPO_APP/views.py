from django.shortcuts import render

# Create your views here.

def UpcomingIPO(request):
    return render(request,'UpcomingIPO.html')

def  broker(request):
    return render(request,'broker.html')

def  all_brokers(request):
    return render(request,'all_brokers.html')

def  community(request):
    return render(request,'community.html')

def  shark_investors(request):
    return render(request,'shark_investors.html')

def  shark_school(request):
    return render(request,'shark_school.html')

def  technical(request):
    return render(request,'technical.html')

def  signIn(request):
    return render(request,'signIn.html')

def  signUp(request):
    return render(request,'signUp.html')

def  forget(request):
    return render(request,'forget.html')
