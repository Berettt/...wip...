from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    haslo2 = forms.CharField(max_length=100,label='Potwierdź hasło:',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Potwierdź hasło'}))
    
    def clean_haslo2(self):
        haslo = self.cleaned_data.get('haslo')
        haslo2 = self.cleaned_data.get('haslo2')
        if haslo and haslo2 and haslo != haslo2:
            raise forms.ValidationError('Hasła nie są identyczne.')
        return haslo2
    
    class Meta:

        model = UserModel
        fields = ['imie','drugie_imie','nazwisko','haslo','haslo2','pesel','data_urodzenia','plec','ulica','kod_pocztowy','miasto','telefon','email']
        labels = {
            'imie': 'Imię',
            'nazwisko': 'Nazwisko',
            'email': 'E-mail',
            'plec': 'Płeć',
            'haslo': 'Hasło',
            'haslo2': 'Potwierdź hasło'
        }
        widgets = {
            'imie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź imię'}),
            'nazwisko': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwisko'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź adres e-mail'}),
            'haslo': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź hasło'})

        }

class LoginForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['email','haslo']
        labels = {'email':'E-mail','haslo':'Hasło'}
        widgets = {
            'email':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź e-mail'}),
            'haslo':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź hasło'})
        }
