from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "html/index.html")

def about(request):
    return render(request, "html/services.html")

def services(request):
    return render(request, "html/about.html")
