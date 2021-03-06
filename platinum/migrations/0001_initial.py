# Generated by Django 3.2.4 on 2021-06-22 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prod_country', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='brands/')),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(blank=True, max_length=50, null=True)),
                ('acea', models.CharField(blank=True, max_length=50, null=True)),
                ('ilsac', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('w_visco', models.IntegerField(default=0)),
                ('s_visco', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='oils/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platinum.brand')),
                ('standards', models.ManyToManyField(related_name='oils', to='platinum.Standard')),
            ],
        ),
    ]
