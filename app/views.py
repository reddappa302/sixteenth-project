from django.shortcuts import render

# Create your views here.
def firstboot(request):
    return render(request,'firstboot.html')