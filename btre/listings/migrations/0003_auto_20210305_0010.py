# Generated by Django 3.1.7 on 2021-03-05 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210304_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
