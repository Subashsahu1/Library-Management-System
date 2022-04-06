from django import forms

# from django.contrib.auth.models import User
from .models import Books,Person,User,Issued


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'isbn', 'author', 'publisher']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'pid', 'email', 'address']


class IssuedBookForm(forms.ModelForm):
    expires_on = forms.DateField(required=False)

    class Meta:
        model = Issued
        fields = ['isbn', 'pid', 'expires_on']
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']