from django.contrib import admin

# Register your models here.
from .models import Imagem


@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    ...