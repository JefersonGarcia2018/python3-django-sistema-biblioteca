from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    data_publicacao = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border border-gray-300 rounded-md mb-4 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'dd/mm/aaaa'
        })
    )
    
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'isbn', 'data_publicacao', 'disponivel']
        # Adicionando classes do Tailwind aos campos
        widgets = {
            field: forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md mb-4'})
            for field in ['titulo', 'isbn']
        }