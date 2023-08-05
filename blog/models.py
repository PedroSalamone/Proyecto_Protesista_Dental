from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.titulo


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    contenido = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}: {self.subject}"



class Delivery(models.Model):
    protesista = models.ForeignKey(User, related_name='deliveries_sent', on_delete=models.CASCADE)
    odontologo = models.ForeignKey(User, related_name='deliveries_received', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.protesista.username} -> {self.odontologo.username}: {self.value}"


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(default='')
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"        




class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo