# Generated by Django 3.0.6 on 2020-05-29 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20200529_2352'),
        ('Fruits', '0001_initial'),
        ('carts', '0003_auto_20200529_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='cart',
            name='own',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customers_cart', to='customers.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='fruit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits_cart', to='Fruits.Fruit'),
        ),
    ]
