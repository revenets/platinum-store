# Generated by Django 3.2.4 on 2021-06-26 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platinum', '0011_alter_cart_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platinum.cart')),
            ],
        ),
    ]
