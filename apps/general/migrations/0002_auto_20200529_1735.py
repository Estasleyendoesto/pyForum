# Generated by Django 3.0.6 on 2020-05-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='comentarios_totales',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='hilos_creados',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='usuarios_registrados',
            field=models.IntegerField(null=True),
        ),
    ]
