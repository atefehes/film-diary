# Generated by Django 4.2.3 on 2023-07-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movielog_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielog',
            name='seen',
            field=models.BooleanField(default=False, verbose_name='seen this film before'),
        ),
    ]
