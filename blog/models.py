from django.db import models

# Create your models here.

from django.utils import timezone


class Post(models.Model): #define nuestro modelo django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #relacion link con otro modelo
    title = models.CharField(max_length=200) #defino un texto con un numero limitado de caracteres
    text = models.TextField() #texto largo sin limite
    created_date = models.DateTimeField( #fecha
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #para definir funciones creadas por mi utilizar minúsculas y guiones bajos en lugar de espacios
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
