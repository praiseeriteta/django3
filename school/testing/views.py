from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "work/home.html")
def about(request):
    return render(request, "work/about.html")
def contact(request):
    return render(request, "work/contact.html")
def blog(request):
    return render(request, "work/blog.html")