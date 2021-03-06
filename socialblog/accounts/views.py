from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # A normal reverse method will automatically navigate to the url without the user signing up.
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
