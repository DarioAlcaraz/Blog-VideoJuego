
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from .forms import ContactForm
from .models import MensajeContacto


class HomeViews(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            nombre = getattr(user, 'nombre', user.username)
            genero = getattr(user, 'genero', 'M')

            saludo = 'Bienvenida' if genero == 'F' else 'Bienvenido'
            context['mensaje'] = f'¡{saludo}, {nombre}!'
        else:
            context['mensaje'] = '¡Bienvenido a mi blog!'
        return context


def Contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            MensajeContacto.objects.create(
                nombre=form.cleaned_data['nombre'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['mensaje']
            )
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})

#probando


def nosotros_view(request):
    return render(request, 'nosotros.html')
