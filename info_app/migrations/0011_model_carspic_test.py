# Generated by Django 2.1 on 2018-09-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0010_auto_20180918_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_carspic',
            name='test',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
    ]
