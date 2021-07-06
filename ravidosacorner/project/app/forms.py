from django.db.models import fields
from .models import FoodItem
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                         SetPasswordForm, PasswordResetForm, 
                                         UserCreationForm, UserChangeForm)
from django.contrib.auth.models import User



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ["username", "password"]


class UserSignupForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}), required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class" : "form-control"}))
    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "email"]


class UserUpdateProfileForm(UserChangeForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}), required=True)
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
    

class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Current Password",
                                   widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(label="New Password",
                                   widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(label="Confirm Password",
                                   widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserForgotPasswordResetForm(PasswordResetForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))


class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password",
                                    widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(label="Confirm Password",
                                    widget=forms.PasswordInput(attrs={"class": "form-control"}))


class FoodItemCreationForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["name", "description", "price", "picture"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "picture": forms.FileInput(attrs={"class": "form-control"}),
        }


class FoodItemUpdationForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["name", "description", "price", "picture"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "picture": forms.FileInput(attrs={"class": "form-control"}),
        }
