# Generated by Django 4.1.7 on 2023-02-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_imagem_image_remove_imagem_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='imagem',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]