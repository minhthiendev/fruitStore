# Generated by Django 3.0.6 on 2020-06-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fruits', '0002_auto_20200530_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefruit',
            name='image',
            field=models.ImageField(upload_to='images/fruit_image/'),
        ),
    ]
