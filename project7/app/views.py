from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'Rani','marks':75}
    return render(request,'conditions.html',d)
