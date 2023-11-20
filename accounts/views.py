from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .forms import UserCreate
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate, login
class SinupPage(CreateView):
    form_class = UserCreate
    template_name = "registration/register.html"
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        form.save()
        username = form.data.get("username")
        password = form.data.get("password1")


        user = authenticate(username=username,password=password)
        if user is not None:
            login(self.request,user)
            return redirect(reverse("home:home"))



        return super().form_valid(form)