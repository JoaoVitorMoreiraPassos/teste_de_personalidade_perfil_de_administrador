# Generated by Django 4.1.7 on 2023-02-14 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_imagem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imagem',
            name='name',
        ),
    ]