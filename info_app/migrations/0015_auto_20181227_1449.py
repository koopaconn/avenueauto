# Generated by Django 2.1.1 on 2018-12-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0014_auto_20181129_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_cars',
            name='moreinfo',
            field=models.CharField(max_length=1000),
        ),
    ]
