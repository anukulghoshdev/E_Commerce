from django.forms import ModelForm
from App_RegLog.models import User, UserProfile

from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)
