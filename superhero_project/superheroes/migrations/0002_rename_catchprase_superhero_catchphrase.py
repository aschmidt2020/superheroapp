# Generated by Django 4.0 on 2021-12-09 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='superhero',
            old_name='catchprase',
            new_name='catchphrase',
        ),
    ]
