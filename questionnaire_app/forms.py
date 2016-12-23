from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    Extend the UserCreationForm to add custom fields.
    """
    username = forms.CharField(label="Your Username")
    password1 = forms.CharField(label="Your Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Your Password", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email Address")
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Surname")

    class Meta:
        """
        Define the order the fields appear on the form.
        """
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2",)

    def save(self, commit=True):
        """
        Override the save method to set the extra fields.
        :param commit: Commit the new user
        :return: User
        """
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            return user
