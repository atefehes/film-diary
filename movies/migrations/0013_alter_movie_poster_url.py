# Generated by Django 4.2.3 on 2023-07-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_movie_poster_movie_poster_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.CharField(max_length=250, null=True),
        ),
    ]