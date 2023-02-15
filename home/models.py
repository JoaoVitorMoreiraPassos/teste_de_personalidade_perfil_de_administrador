from django.db import models

# Create your models here.


class Imagem(models.Model):
    name = models.CharField(max_length=128, default="")
    image = models.ImageField(upload_to="home/", default="")
