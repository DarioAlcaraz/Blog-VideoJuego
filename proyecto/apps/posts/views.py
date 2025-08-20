# apps/posts/views.py

# 📦 Imports estándar
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q

# 🧱 Vistas genéricas
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin

# 📁 Modelos y formularios propios
from .models import Post, Categoria
from .forms import PostForm

# 💬 Opiniones
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

# -------------------------------------------------------------------
# 📚 Vista: Listar Posts con filtros
# -------------------------------------------------------------------
class ListarPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset().filter(activo=True)
        categoria = self.request.GET.get('categoria')
        orden = self.request.GET.get('orden', '-publicado')
        busqueda = self.request.GET.get('q')

        if categoria:
            queryset = queryset.filter(categoria__nombre=categoria)

        if busqueda:
            queryset = queryset.filter(
                Q(titulo__icontains=busqueda) |
                Q(subtitulo__icontains=busqueda) |
                Q(texto__icontains=busqueda)
            )

        return queryset.order_by(orden)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['categoria_actual'] = self.request.GET.get('categoria', 'Todas')
        context['orden_actual'] = self.request.GET.get('orden', '-publicado')
        context['busqueda_actual'] = self.request.GET.get('q', '')
        return context

# -------------------------------------------------------------------
# 📝 Vista: Crear Post
# -------------------------------------------------------------------
class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crear_post.html'
    success_url = reverse_lazy('posts:posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "¡Publicación creada exitosamente!")
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.warning(self.request, "Tenés que iniciar sesión para crear una publicación.")
        return redirect('usuarios:iniciar_sesion')

# -------------------------------------------------------------------
# ✏️ Vista: Actualizar Post
# -------------------------------------------------------------------
class ActualizarPost(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'editar_post.html'
    success_url = reverse_lazy('posts:posts')

    def form_valid(self, form):
        messages.success(self.request, "¡Publicación actualizada correctamente!")
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.autor != request.user:
            messages.error(request, "No tenés permiso para modificar esta publicación.")
            return redirect('posts:posts')
        return super().dispatch(request, *args, **kwargs)

# -------------------------------------------------------------------
# 🗑️ Vista: Eliminar Post
# -------------------------------------------------------------------
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('posts:posts')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Publicación eliminada con éxito.")
        return super().delete(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.autor != request.user:
            messages.error(request, "No tenés permiso para eliminar esta publicación.")
            return redirect('posts:posts')
        return super().dispatch(request, *args, **kwargs)

# -------------------------------------------------------------------
# 🔍 Vista: Detalle del Post + Opiniones
# -------------------------------------------------------------------
class DetallePost(DetailView):
    model = Post
    template_name = 'posts/detalle_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['opiniones'] = Opinion.objects.filter(post=self.object)
        if self.request.user.is_authenticated:
            context['form'] = OpinionForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = OpinionForm(request.POST)
        if form.is_valid():
            nueva_opinion = form.save(commit=False)
            nueva_opinion.usuario = request.user
            nueva_opinion.post = self.object
            nueva_opinion.save()
            messages.success(request, "¡Tu opinión fue publicada!")
            return redirect('posts:detalle_post', pk=self.object.pk)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)