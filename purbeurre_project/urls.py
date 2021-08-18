"""purbeurre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include, url
from users import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth_views


# urlpatterns = [
#     # home route
#     path("", views.index, name="index"),
#     url(r'^purbeurre/', include(('purbeurre.urls', 'purbeurre'), namespace='purbeurre')),
#     path('users/', include('users.urls', namespace="users")),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path("", views.index, name="index"),
    path("password_reset",auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html",),name="password_reset",),
    path("password-reset/done",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done",),
    re_path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name="password_reset_confirm",),
    path("password_reset/complete",auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html",),name="password_reset_complete",),

]

urlpatterns += i18n_patterns(
    path("", views.index, name="index"),
    re_path(r'^purbeurre/', include(('purbeurre.urls', 'purbeurre'), namespace='purbeurre')),
    path('users/', include('users.urls', namespace="users")),
    path("password-reset/done",auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done",),

    
)
