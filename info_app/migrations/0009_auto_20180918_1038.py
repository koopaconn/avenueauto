# Generated by Django 2.1 on 2018-09-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0008_auto_20180918_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_carspic',
            name='pic',
            field=models.ImageField(upload_to='info_app/media/'),
        ),
    ]
