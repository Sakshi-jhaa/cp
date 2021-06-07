# Generated by Django 3.2.2 on 2021-06-05 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0023_auto_20210604_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resname', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('amount', models.FloatField(null=True)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='capp.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurants',
        ),
        migrations.DeleteModel(
            name='menu',
        ),
        migrations.DeleteModel(
            name='restaurant',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='capp.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='capp.category'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='capp.product'),
        ),
    ]
