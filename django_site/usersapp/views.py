from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import StandardUser
from rest_framework.authtoken.models import Token


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'

class UserCreateView(CreateView):
    model = StandardUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')
    
class UserCreateView(CreateView):
    model = StandardUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')
    
class UserDetailView(DetailView):
    template_name = 'usersapp/profile.html'
    model = StandardUser

def update_token(request):
    user = request.user
    if user.auth_token:
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))