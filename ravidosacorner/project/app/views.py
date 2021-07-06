from app.models import FoodItem
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.forms.widgets import EmailInput
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import View
from .forms import (UserLoginForm, UserChangePasswordForm,
                     UserForgotPasswordResetForm, UserPasswordResetConfirmForm,
                      UserSignupForm, UserUpdateProfileForm, 
                      FoodItemCreationForm, FoodItemUpdationForm)

from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


class UserLoginView(LoginView):
    template_name = "app/registration/login.html"
    authentication_form = UserLoginForm


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserSignupForm
    template_name = "app/registration/create_user.html"
    success_message = "Record Created successfully!"
    # context_object_name = "form"

    def get_success_url(self):
        return reverse("signup")


@method_decorator(login_required, name="dispatch")
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateProfileForm
    template_name = "app/registration/update_user.html"
    success_message = "Record Updated successfully!"
    # context_object_name = "form"

    def get_success_url(self, **kwargs):
        return reverse("profile", kwargs={ "pk" : self.object.pk })


@method_decorator(login_required, name="dispatch")
class UserPasswordChangeView(PasswordChangeView):
    template_name = "app/registration/password_change.html"
    form_class = UserChangePasswordForm


class UserPasswordResetView(PasswordResetView):
    template_name="app/registration/password_reset.html"
    form_class = UserForgotPasswordResetForm
    html_email_template_name = 'app/registration/password_reset_email.html'
    # email_template_name = 'app/registration/password_reset_email.html'
    # subject_template_name = 'app/registration/password_reset_subject.txt'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "app/registration/password_reset_confirm.html"
    form_class = UserPasswordResetConfirmForm
    # post_reset_login = False
    # post_reset_login_backend = None


# ==========================================================================


class IndexTemplateView(TemplateView):
    template_name = "app/index.html"    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["name"] = "Amit"
        # context["salary"] = 12000
        # context["id"] = kwargs["id"]
        return context


class AboutUsTemplateView(TemplateView):
    template_name = "app/aboutus.html"    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["name"] = "Amit"
        # context["salary"] = 12000
        # context["id"] = kwargs["id"]
        return context


class FoodItemListView(ListView):
    model = FoodItem
    template_name = "app/specials.html"    
    context_object_name = "specials"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["name"] = "Amit"
        # context["salary"] = 12000
        # context["id"] = kwargs["id"]
        return context


@method_decorator(login_required, name="dispatch")
class FoodItemCreateView(SuccessMessageMixin, CreateView):
    form_class = FoodItemCreationForm
    template_name = "app/dashboard.html"
    success_message = "Food Item Added successfully!"
    context_object_name = "form"

    def get_success_url(self):
        return reverse("dashboard")


@method_decorator(login_required, name="dispatch")
class FoodItemUpdateView(SuccessMessageMixin, UpdateView):
    model = FoodItem
    form_class = FoodItemUpdationForm
    template_name = "app/update_fooditem.html"    
    success_message = "Food Item Updated successfully!"
    # context_object_name = "special"

    def get_success_url(self, **kwargs):
        return reverse("update", kwargs={ "pk" : self.object.pk })


@method_decorator(login_required, name="dispatch")
class FoodItemDeleteView(DeleteView):
    model = FoodItem
    template_name = "app/delete_fooditem.html"    
    context_object_name = "special" 

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Food Item Deleted successfully")        
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("specials")

