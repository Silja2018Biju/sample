from django.shortcuts import render

# Create your views here.
def loadfirstpage(request):
    return render(request,'static1.html')

def loadsecondpage(request):
    return render(request,'static2.html')

