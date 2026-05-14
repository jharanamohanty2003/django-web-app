from django.shortcuts import render

# Create your views here.
def genericStatic(request):
    return render(request,'genericStatic.html')
