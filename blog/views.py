from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost, Message, Delivery, Publicacion, Comentario, Noticia
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, MessageForm, UserProfileForm, UserRegistrationForm, LoginForm, ComentarioForm, PublicacionForm, NoticiaForm
from django.contrib.auth.hashers import make_password



def inicio_view(request):
    return render(request, 'blog/inicio.html')


def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_blog_post.html', {'form': form})


@csrf_exempt
def blog_post_list_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/blog_post_list.html', {'blog_posts': blog_posts})



def blog_post_detail_view(request, pk):
    blog_post = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=blog_post)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            if request.user.is_authenticated:
                comentario = comentario_form.save(commit=False)
                comentario.publicacion = blog_post
                comentario.autor = request.user
                comentario.save()

                
                comentarios = Comentario.objects.filter(publicacion=blog_post)

                return redirect('blog:blog_post_detail', pk=pk)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'blog/blog_post_detail.html', {'blog_post': blog_post, 'comentarios': comentarios, 'comentario_form': comentario_form})




def user_register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:lista_publicaciones')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/user_register.html', {'form': form})



def user_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:lista?publicaciones')
            else:
                form.add_error(None, 'Datos Incorrectos. Intenta de Nuevo...')
    else:
        form = LoginForm()
        
    return render(request, 'blog/user_login.html', {'form': form})


@login_required
def user_profile_edit_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:user_profile')  
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/user_profile_edit.html', {'form': form})


@login_required
def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'blog/user_profile.html', {'user': request.user})



@login_required
def send_message_view(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = recipient
            message.save()
            return redirect('blog:inbox')
    else:
        form = MessageForm()
    return render(request, 'blog/send_message.html', {'form': form, 'recipient': recipient})

@login_required
def inbox_view(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'blog/inbox.html', {'messages': messages})

@login_required
def message_detail_view(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    return render(request, 'blog/message_detail.html', {'message': message})



def acerca_de_mi_view(request):
    return render(request, 'blog/acerca_de_mi.html')



def contacto_view(request):
    contact_data = {
        'nombre': 'ProDental',
        'email': 'prodental@pipomail.com',
    }
    return render(request, 'blog/contacto.html', {'contact_data': contact_data})



def page_not_found_view(request, exception):
    return render(request, 'blog/error_404.html', status=404)


def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    form = PublicacionForm()
    
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('blog:lista_publicaciones')
    
    return render(request, 'blog/lista_publicaciones.html', {'publicaciones': publicaciones, 'form': form})


def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = Comentario.objects.filter(publicacion=publicacion)

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect('blog:blog_post_detail', pk=pk)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'blog/blog_post_detail.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'comentario_form': comentario_form})


def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            contenido = form.cleaned_data['contenido']
            imagen = form.cleaned_data['imagen']
            
            if Publicacion.objects.filter(titulo=titulo, contenido=contenido, imagen=imagen).exists():
                messages.error(request, 'La publicación ya existe.')
                return redirect('blog:lista_publicaciones')
            
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request, 'La publicación ha sido creada exitosamente.')
            return redirect('blog:lista_publicaciones')
    else:
        form = PublicacionForm()
    
    return render(request, 'blog/crear_publicacion.html', {'form': form})


def busqueda_publicacion_view(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            publicaciones = Publicacion.objects.filter(titulo__icontains=query)
        else:
            publicaciones = Publicacion.objects.all()
    else:
        publicaciones = Publicacion.objects.all()

    # Asegúrate de pasar el contexto adecuado aquí
    context = {
        'publicaciones': publicaciones,
        'query': query,
    }

    return render(request, 'blog/busqueda_publicacion.html', context)



def noticias_view(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect('blog:noticias')
    else:
        form = NoticiaForm()
    noticias = Noticia.objects.all()
    return render(request, 'blog/noticias.html', {'form': form, 'noticias': noticias})



def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticias')  
    else:
        form = NoticiaForm()
    return render(request, 'blog/agregar_noticia.html', {'form': form})