# Generated by Django 3.1.7 on 2021-06-27 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0008_score_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
    ]
