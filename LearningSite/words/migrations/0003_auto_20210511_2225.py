# Generated by Django 3.1.7 on 2021-05-11 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20210321_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meaning',
            old_name='enlish_sentences',
            new_name='english_sentences',
        ),
    ]
