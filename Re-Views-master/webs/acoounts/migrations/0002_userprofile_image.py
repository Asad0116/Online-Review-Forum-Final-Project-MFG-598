# Generated by Django 2.1.7 on 2019-03-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]