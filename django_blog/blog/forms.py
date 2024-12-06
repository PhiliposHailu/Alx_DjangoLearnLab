from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model

class UserRegisteration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = '__all__'

# This basically overrides the save function in order to save the email in to the database
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
