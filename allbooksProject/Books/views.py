from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  
    template_name = 'Books/signup.html' 


def home(request):
    return render(request, "Books/index.html")

def forgot_password(request):
    return render(request, "Books/forgotPassword.html")

def purchase(request):
    return render(request, "Books/purchase.html")

def about(request):
    return render(request, "Books/about.html")
<<<<<<< HEAD

def blog(request):
    return render(request, "Books/blog.html")

def contact(request):
    return render(request, "Books/contact.html")

=======
def contact(request):
    return render(request, "Books/contact.html")
>>>>>>> 50179ff48abff987a95e9a533c2c34ab9ee48a30
'''
def login(request):
    return render(request, "Books/login.html")
'''