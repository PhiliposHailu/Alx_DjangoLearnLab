from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post
# from django.contrib.auth import get_user_model

# User = get_user_model

# class UserRegisteration(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = '__all__'

# # This basically overrides the save function in order to save the email in to the database
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        # def save(self, commit=True, user=None):
        #     instance = super().save(commit=False)

        #     if user:
        #         instance.author = user

        #     if commit:
        #         instance.save()

        #     return instance