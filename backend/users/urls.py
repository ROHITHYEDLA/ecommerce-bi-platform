from django.urls import path

from .views import (
    RegisterUserView,
    LoginView,
    UserProfileView,
    UserProfileUpdateView,
    ChangePasswordView,
    LogoutView,
    ForgotPasswordView,
    ResetPasswordView
)
urlpatterns = [
    path(
        "register/",
        RegisterUserView.as_view(),
        name="register",
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),

    path(
        "profile/",
        UserProfileView.as_view(),
        name="profile",
    ),
    path(
        "profile/update/",
        UserProfileUpdateView.as_view(),
        name="profile-update",
    ),
    path(
        "change-password/", 
        ChangePasswordView.as_view(), 
        name="change-password",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot-password",
    ),
    path(
        "reset-password/",
        ResetPasswordView.as_view(),
        name="reset-password",
    ),

]