# Generated by Django 2.1.2 on 2018-11-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20181125_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='video',
            field=models.ManyToManyField(blank=True, to='base.Resource'),
        ),
    ]
