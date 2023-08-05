from django import forms
from .models import BlogPost, Message, Comentario, Publicacion, Noticia
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True, help_text='Ingresa tu correo electrónico')
    username = forms.CharField(max_length=150, required=True, help_text='Ingresa tu nombre de usuario')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), required=True)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'fecha_publicacion', 'imagen']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'contenido']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'imagen', 'autor']



class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'imagen']
