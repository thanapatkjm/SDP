# Generated by Django 2.1.1 on 2019-01-16 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalSite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='descript',
            new_name='animal',
        ),
    ]
