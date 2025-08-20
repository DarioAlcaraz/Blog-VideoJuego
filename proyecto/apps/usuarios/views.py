from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario
from .forms import RegistroUsuarioForm

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import ActualizarUsuarioForm



# 🏠 Página principal de la app usuarios
def index(request):
    return render(request, 'usuarios/index.html')

# 📝 Registro de usuario
class RegistroUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registrar.html'
    success_url = reverse_lazy('index')

# 👥 Listado de usuarios
@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuario.html', {'usuarios': usuarios})




# ✏️ Actualizar perfil


class ActualizarUsuario(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = ActualizarUsuarioForm
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if str(user_id) != str(request.user.pk) and not request.user.is_superuser:
            raise Http404("No tienes permiso para actualizar este usuario")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente')
        return super().form_valid(form)

# 🗑️ Eliminar usuario
class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = "usuarios/confirmar_eliminar.html"
    success_url = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if str(user_id) != str(request.user.pk) and not request.user.is_superuser:
            raise Http404("No tienes permiso para eliminar este usuario")
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Tu cuenta ha sido eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
    



class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('inicio')






