# Generated by Django 3.1.7 on 2021-03-21 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='Vocabulary',
        ),
        migrations.RenameField(
            model_name='meaning',
            old_name='character',
            new_name='vocabulary',
        ),
    ]