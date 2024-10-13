from django.shortcuts import render
from django.views import View
from .forms import loginForm,registrationForm,emailForm,resetForm
from .models import userInfo
from django.http import HttpResponseRedirect
from django.urls import reverse
from .helper import send_reset_link
import uuid
from django.contrib import messages

# Create your views here.

class UserLoginView(View):
    
    def get(self,request):
        loginform = loginForm
        return render(request,"login_and_signup/login.html",{
            "loginForm" : loginform,
        })
    
    def post(self,request):
        form = loginForm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request,"login_and_signup/login.html",{
                "loginForm" : form,
            })


class UserRegisterView(View):
    def get(self,request):
        registerForm = registrationForm()
        return render(request,"login_and_signup/register.html",{
            "registerForm" : registrationForm
        })
        
    def post(self, request):
        form = registrationForm(request.POST)
        
        if form.is_valid():
            saveInfo = userInfo(firstName=form.cleaned_data['firstName'],lastName=form.cleaned_data['lastName'],emailAddress=form.cleaned_data['email'],password=form.cleaned_data['password'])
            saveInfo.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request,"login_and_signup/register.html",{
                "registerForm" : form,
            })
            
class resetView(View):
    def get(self,request):
        Form = emailForm()
        return render(request,"login_and_signup/reset.html",{
            "Form" :Form,
        })
        
    def post(self,request):
        form = emailForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            send_reset_link(email)
            messages.success(request,"Check Your Mail!")
            return render(request,"login_and_signup/reset.html",{
            "Form" :form,
        })
        else:
            return render(request,"login_and_signup/reset.html",{
            "Form" :form,
        })
            
            
class changePassView(View):
    def get(self,request,email):
        Form = resetForm()
        return render(request,"login_and_signup/setpass.html",{
            "email":email,
            "Form": Form,
        })
        
    def post(self,request,email):
        form = resetForm(request.POST)

        if form.is_valid():
            newpassword = form.cleaned_data['newpassword']
            user = userInfo.objects.filter(emailAddress=email)[0]
            user.password = newpassword
            user.save()
            return HttpResponseRedirect(reverse("login"))

            
        
            
            