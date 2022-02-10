from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "html/index.html")

def about(request):
    return render(request, "html/about.html")

def services(request):
    return render(request, "html/services.html")

def contact(request):
    return render(request, "html/contact.html")

