# Generated by Django 3.0.6 on 2020-05-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='frase',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]