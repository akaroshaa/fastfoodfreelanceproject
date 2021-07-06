from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    
    path('', views.IndexTemplateView.as_view(), name="index"),
    path('specials/', views.FoodItemListView.as_view(), name="specials"),
    path('aboutus/', views.AboutUsTemplateView.as_view(), name="aboutus"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="app/registration/logout.html"), name="logout"),
    path('signup/', views.UserCreateView.as_view(), name="signup"),
    path('profile/<int:pk>/', views.UserUpdateView.as_view(), name="profile"),
    path('dashboard/', views.FoodItemCreateView.as_view(), name="dashboard"),
    path('update/<int:pk>/', views.FoodItemUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', views.FoodItemDeleteView.as_view(), name="delete"),
    
    # exact password change urls
    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="app/registration/password_change_done.html"), name='password_change_done'),


    # ===========================================================================================================

    #       >>>>>>>>>>>>>>>> custom password change urls <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # path('change_password/', auth_views.PasswordChangeView.as_view(template_name="app/registration/password_change.html", success_url="/done/password_change/"), name='change_password'),
    # path('done/password_change/', auth_views.PasswordChangeDoneView.as_view(template_name="app/registration/password_change_done.html"), name='done_password_change'),

    #       >>>>>>>>>>>>>>>>>>>>>>> explanation <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # by default, after changing the password, it searches for "password_change_done" but we 
    # need to override the "success_url" to make it search for "done_password_change"

    # ===========================================================================================================


    path('password_reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="app/registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="app/registration/password_reset_complete.html"), name='password_reset_complete'),


]

