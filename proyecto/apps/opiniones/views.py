from django.shortcuts import get_object_or_404, render, redirect
from .models import Opinion
from .forms import OpinionForm
from apps.posts.models import Post  # ✅ Asegúrate de que el modelo Post esté en la app 'posts'

# Vista para agregar una opinión desde una plantilla separada
def agregar_opinion(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.usuario = request.user
            opinion.post = post
            opinion.save()
            return redirect('opiniones:detalle_post', post_id=post.id)
    else:
        form = OpinionForm()

    return render(request, 'opiniones/agregar_opinion.html', {'form': form, 'post': post})

# Vista para mostrar el detalle del post y sus opiniones
def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    opiniones = Opinion.objects.filter(post=post).order_by('-fecha')

    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.usuario = request.user
            opinion.post = post
            opinion.save()
            return redirect('opiniones:detalle_post', post_id=post.id)
    else:
        form = OpinionForm()

    context = {
        'post': post,
        'opiniones': opiniones,
        'form': form,
    }
    return render(request, 'posts/detalle_post.html', context)


def lista_opiniones(request):
    opiniones = Opinion.objects.select_related('post', 'usuario').all()
    return render(request, 'opiniones/lista_opiniones.html', {'opiniones': opiniones})