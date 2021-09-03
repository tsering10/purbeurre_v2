from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.sign_up, name='sign_up'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('account/', views.account, name='account'),
    path('saved/', views.saved, name='saved'),
    path("password_reset",auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html",),name="password_reset",),
    path("password-reset/done",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done",),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name="password_reset_confirm",),
    path("password_reset/complete", auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html",),name="password_reset_complete",),
]
