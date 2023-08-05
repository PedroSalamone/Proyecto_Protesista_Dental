from django.contrib import admin
from .models import BlogPost, Message, Delivery, Publicacion, Comentario, Noticia
from .apps import BlogConfig


admin.site.register(BlogPost)
admin.site.register(Message)
admin.site.register(Delivery)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Noticia)
admin.site.site_header = 'Protesista Dental Admin'
admin.site.site_title = 'Protesista Dental Admin'
admin.site.index_title = 'Bienvenidx al Panel de Administración del Protesista Dental'


