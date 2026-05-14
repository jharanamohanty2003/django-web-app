from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={'name':'Rani','age':22}
    return render(request,'jinjaprint.html',context=d)
