# Generated by Django 2.1 on 2018-09-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0009_auto_20180918_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_carspic',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
