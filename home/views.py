from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
class HomePageView(LoginRequiredMixin,TemplateView):
   template_name = 'index.html'

class ChatbotView(LoginRequiredMixin,TemplateView):
   template_name = 'bot.html'

class ProfilebotView(LoginRequiredMixin,TemplateView):
   template_name = 'profile.html'

class LoginbotView(LoginRequiredMixin,TemplateView):
    template_name = 'registration/login.html'


class RegisterbotView(LoginRequiredMixin,TemplateView):
   template_name = 'register.html'