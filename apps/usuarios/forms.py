import re
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class LoginFormsAdm(forms.Form):
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
        ) # widget=forms.PasswordInput is used to hide the password
    
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
        ) # widget=forms.PasswordInput is used to hide the password
    
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
        ) # widget=forms.PasswordInput is used to hide the password 
    
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

class LoginFormsPa(forms.Form):
    cpf = forms.CharField(
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
        ) # widget=forms.PasswordInput is used to hide the password
    
CustomUser = get_user_model()

class CadastroFormsPa(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'cpf']

    username = forms.CharField(
        label='Nome de Login:',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joaozinho123'
            }
        )
    )

    cpf = forms.CharField(
        label='CPF:',
        required=True,
        max_length=11,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Apenas números'
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
        ) # widget=forms.PasswordInput is used to hide the password
    
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
        ) # widget=forms.PasswordInput is used to hide the password 
    
    def clean_nomeCadastro(self):
        nome = self.cleaned_data.get('nomeCadastro')

        if nome:
            nome = nome.strip() #strip() tira os espaços em branco do começo e do final da string
            if ' ' in nome:
                raise forms.ValidationError('O nome de usuário não pode conter espaços')
            else:
                return nome
            
    def clean_cpfCadastro(self):
        cpf = self.cleaned_data.get('cpfCadastro')
        if not re.match(r'^\d{11}$', cpf):
            raise forms.ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf
            
    def clean_senhaCadastro2(self):
        senha = self.cleaned_data.get('senhaCadastro')
        senha2 = self.cleaned_data.get('senhaCadastro2')
    
        if senha and senha2:
            if senha != senha2:
                raise forms.ValidationError('As senhas não são iguais')
            else:
                return senha2

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not re.match(r'^\d{11}$', cpf):
            raise forms.ValidationError('CPF deve conter exatamente 11 dígitos.')
        return cpf