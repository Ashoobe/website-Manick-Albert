from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "Books/index.html")

def login(request):
    return render(request, "Books/login.html")
