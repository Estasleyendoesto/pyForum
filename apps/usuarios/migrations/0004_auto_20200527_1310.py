# Generated by Django 3.0.6 on 2020-05-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_usuario_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='photo',
            field=models.ImageField(default='users/default.jpg', upload_to='users/'),
        ),
    ]
