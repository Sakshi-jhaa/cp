# Generated by Django 3.2 on 2021-05-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0007_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
