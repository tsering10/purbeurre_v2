from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.utils.translation import ugettext_lazy as _


class UserRegisterForm(UserCreationForm):
    """Customize register formulaire"""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@email.com",
            }
        ),
    )
    username = forms.CharField(
        label=_("Nom de l'utilisateur"),
        widget=forms.TextInput(
            attrs={
                "placeholder": "nom d'utilisateur",
            }
        ),
    )

    password1 = forms.CharField(
        label= _("Mot de passe"),
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mot de passe",
                "type": "password",
            }
        ),
    )

    password2 = forms.CharField(
        label=_("Confirmation de votre de passe"),
        widget=forms.TextInput(
            attrs={
                "placeholder": "Confirmation",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]