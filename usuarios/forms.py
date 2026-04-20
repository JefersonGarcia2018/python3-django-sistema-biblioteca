from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario
from django import forms
import uuid

class UsuarioCreationForm(UserCreationForm):
    first_name = forms.CharField(label="Nome", max_length=30)
    last_name = forms.CharField(label="Sobrenome", max_length=150)
    email = forms.EmailField(label="E-mail", required=True)

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        # Add a quiet randomly generated username since Django requires it natively.
        user.username = str(uuid.uuid4())[:30] 
        if commit:
            user.save()
        return user
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all outline-none mb-3'


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all outline-none mb-3'
