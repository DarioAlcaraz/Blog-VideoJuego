from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['autor']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título épico del post',
            }),
            'subtitulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtítulo con estilo gamer',
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Escribí tu reseña, análisis o historia gamer...',
                'style': 'resize: vertical;'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }