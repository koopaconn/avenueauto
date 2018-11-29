# Generated by Django 2.1.1 on 2018-11-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0013_model_cars_headpic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_cars',
            name='color',
        ),
        migrations.AddField(
            model_name='model_cars',
            name='MSRP',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_cars',
            name='savings',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_cars',
            name='transmission',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_cars',
            name='vin',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
    ]