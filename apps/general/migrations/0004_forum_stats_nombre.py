# Generated by Django 3.0.6 on 2020-05-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20200529_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum_stats',
            name='nombre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]