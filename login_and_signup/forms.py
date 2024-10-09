from typing import Any
from django import forms
from .validators.validators import LowercaseValidator,NumberValidator,SymbolValidator,UppercaseValidator
from .models import userInfo


class registrationForm(forms.Form):
    firstName = forms.CharField(max_length=150,label="First Name")
    lastName = forms.CharField(max_length=150,label="Last Name")
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(max_length=30,min_length=8,label="Password",widget=forms.PasswordInput,validators=[LowercaseValidator(),NumberValidator(),SymbolValidator(),UppercaseValidator()])
    confirmPassword = forms.CharField(max_length=30,min_length=8,widget=forms.PasswordInput,label="Confirm Password")
    
    def clean(self):
        cleaned_data =  super().clean()
        password = cleaned_data.get("password")
        confirmPassword = cleaned_data.get("confirmPassword")
        email = cleaned_data.get('email')
        
        if password and confirmPassword and (password != confirmPassword):
            self.add_error('confirmPassword',"Your password doesn't match, Please enter matching password")
            
        if userInfo.objects.filter(emailAddress=email).exists():
            self.add_error('email',"Email already exists, Try with another email ID!")
    
class loginForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(max_length=30,min_length=8,label="Password",widget=forms.PasswordInput,validators=[LowercaseValidator(),UppercaseValidator(),SymbolValidator(),NumberValidator()])
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        userlist = userInfo.objects.filter(emailAddress=email)
        user = userlist[0] if userlist.exists() else None
        
        if user == None:
            self.add_error('email',"Email does not exists.")
        else:
            if user.password != password:
                self.add_error('password',"Invalid Password!")

            
class emailForm(forms.Form):
    email = forms.EmailField(label="Enter Registered Email")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        
        userlist = userInfo.objects.filter(emailAddress=email)
        user = userlist[0] if userlist.exists() else None
        if user == None:
            self.add_error('email',"Email not regestered!")
    
    
class resetForm(forms.Form):
    newpassword = forms.CharField(max_length=30,min_length=8,label="New Password",widget=forms.PasswordInput,validators=[LowercaseValidator(),NumberValidator(),SymbolValidator(),UppercaseValidator()])
    confirmPassword = forms.CharField(max_length=30,min_length=8,widget=forms.PasswordInput,label="Confirm Password")
    
    def clean(self):
        cleaned_data =  super().clean()
        newpassword = cleaned_data.get("password")
        confirmPassword = cleaned_data.get("confirmPassword")
        
        if newpassword and confirmPassword and (newpassword != confirmPassword):
            self.add_error('confirmPassword',"Your password doesn't match, Please enter matching password")
