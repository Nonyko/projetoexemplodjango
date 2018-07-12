from django import forms

class PessoaForm(forms.Form):
    nome = forms.CharField(label='nome')
    email = forms.EmailField(label='e-mail')