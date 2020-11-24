from django.shortcuts import render

# Create your views here.
def qr_home (request):
    return render(request,'Scanner.html',context={})