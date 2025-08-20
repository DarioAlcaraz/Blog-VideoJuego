from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
