import re
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    username = forms.CharField(
        label='Nome de Login:',
        required= True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joaozinho123'
                }
            )
    )
    senha = forms.CharField(
        label='Senha:',
        required= True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
                }
            )
        ) 
    
class CadastroFormsAdm (forms.Form):
    nomeCadastro = forms.CharField(
        label='Nome de Login:',
        required= True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joaozinho123'
                }
            )
    )

    emailCadastro = forms.EmailField(
        label='Email:',
        required= True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
                }
            )
    )

    senhaCadastro = forms.CharField(
        label='Senha:',
        required= True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha:'
                }
            )
        ) 
    
    senhaCadastro2 = forms.CharField(
        label='Confirme sua senha:',
        required= True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
                }
            )
        ) 
    
    def clean_nomeCadastro(self):
        nome = self.cleaned_data.get('nomeCadastro')

        if nome:
            nome = nome.strip() #strip() tira os espaços em branco do começo e do final da string
            if ' ' in nome:
                raise forms.ValidationError('O nome de usuário não pode conter espaços')
            else:
                return nome
            
    def clean_senhaCadastro2(self):
        senha = self.cleaned_data.get('senhaCadastro')
        senha2 = self.cleaned_data.get('senhaCadastro2')
    
        if senha and senha2:
            if senha != senha2:
                raise forms.ValidationError('As senhas não são iguais')
            else:
                return senha2
            
class CadastroFormsPa(forms.Form):
    nomeCadastro = forms.CharField(
        label='Nome de Login:',
        required= True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joaozinho123'
                }
            )
    )

    emailCadastro = forms.EmailField(
        label='Email:',
        required= True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
                }
            )
    )

    senhaCadastro = forms.CharField(
        label='Senha:',
        required= True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha:'
                }
            )
        ) 
    
    senhaCadastro2 = forms.CharField(
        label='Confirme sua senha:',
        required= True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
                }
            )
        ) 
    
    def clean_nomeCadastro(self):
        nome = self.cleaned_data.get('nomeCadastro')

        if nome:
            nome = nome.strip() #strip() tira os espaços em branco do começo e do final da string
            if ' ' in nome:
                raise forms.ValidationError('O nome de usuário não pode conter espaços')
            else:
                return nome
            
    def clean_senhaCadastro2(self):
        senha = self.cleaned_data.get('senhaCadastro')
        senha2 = self.cleaned_data.get('senhaCadastro2')
    
        if senha and senha2:
            if senha != senha2:
                raise forms.ValidationError('As senhas não são iguais')
            else:
                return senha2