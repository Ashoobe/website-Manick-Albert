from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    #path("login/", views.login,name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='Books/login.html'), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('purchase/', views.purchase, name='purchase'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('forgotpassword/', views.forgot_password, name='forgotpassword'),
    path('about/', views.about, name = 'about'),
]