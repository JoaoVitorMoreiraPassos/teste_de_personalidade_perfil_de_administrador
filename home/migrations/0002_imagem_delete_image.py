# Generated by Django 4.1.7 on 2023-02-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
