from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Search for a book'})
    )