# Generated by Django 3.0.6 on 2020-05-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20200529_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]