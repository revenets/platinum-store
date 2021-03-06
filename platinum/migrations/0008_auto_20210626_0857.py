# Generated by Django 3.2.4 on 2021-06-26 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platinum', '0007_oilinstance_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oil',
            options={'ordering': ['brand']},
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, null=True)),
                ('oil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='platinum.oilinstance')),
            ],
        ),
    ]
