from django.forms import ModelForm
from models import User, Profile


class UserForm(ModelForm):
    class Meta:
        model = User


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
