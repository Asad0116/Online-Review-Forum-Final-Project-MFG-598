# Generated by Django 2.1.7 on 2019-03-18 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20190313_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(choices=[('Hospital', 'Hospital'), ('College', 'College'), ('Hotel', 'Hotel'), ('Restaurants', 'Restaurants'), ('Movies', 'Movies')], default='', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='bang',
            name='category',
        ),
        migrations.AddField(
            model_name='bang',
            name='category',
            field=models.ManyToManyField(blank=True, to='forum.Category'),
        ),
    ]