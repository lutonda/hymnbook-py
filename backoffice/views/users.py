from django.shortcuts import render

# Create your views here.
def new (request):
    return render(request,'users/new.html')

def list (request):
    return render(request,'users/list.html',{'core_logout':''})

def update (request):
    return
