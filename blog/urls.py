from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_login_view, user_register_view, busqueda_publicacion_view

app_name = 'blog'

urlpatterns = [
    #path('', views.index_view, name='index'),
    path('', views.inicio_view, name='inicio'),
    path('login/', views.user_login_view, name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('lista_publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('blog_post/<int:pk>/', views.blog_post_detail_view, name='blog_post_detail'),
    path('user_profile_edit/', views.user_profile_edit_view, name='user_profile_edit'),
    path('send_message/<int:recipient_id>/', views.send_message_view, name='send_message'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('message_detail/<int:message_id>/', views.message_detail_view, name='message_detail'),
    path('busqueda_publicacion/', views.busqueda_publicacion_view, name='busqueda_publicacion'),
    path('user_register/', views.user_register_view, name='user_register'),
    path('acerca_de_mi/', views.acerca_de_mi_view, name='acerca_de_mi'),
    path('contacto/', views.contacto_view, name='nombre_de_la_vista_de_contacto'),
    #path('blog/', views.lista_publicaciones, name='blog_post_list'),
    #path('blog-post/<int:pk>/', views.detalle_publicacion, name='blog_post_detail'),
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('noticias/', views.noticias_view, name='noticias'),
    path('agregar_noticia/', views.agregar_noticia, name='agregar_noticia'),
]