from django.shortcuts import render
from django.views import View


class SignInView(View):
    def get(self, request):
        return render(request, "signin.html")


class SignUpView(View):
    def get(self, request):
        return render(request, "signup.html")
