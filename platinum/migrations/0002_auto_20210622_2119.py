# Generated by Django 3.2.4 on 2021-06-22 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platinum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standard',
            name='acea',
        ),
        migrations.RemoveField(
            model_name='standard',
            name='api',
        ),
        migrations.RemoveField(
            model_name='standard',
            name='ilsac',
        ),
    ]
