# Generated by Django 2.1.7 on 2019-03-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_remove_bang_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bang',
            name='review',
            field=models.TextField(default='', max_length=100),
        ),
    ]
