# Generated by Django 5.1.4 on 2025-01-17 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_musician_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alive',
            old_name='died',
            new_name='place_of_birth',
        ),
    ]
