# Generated by Django 2.2.18 on 2021-02-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0005_auto_20210211_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='img',
            field=models.ImageField(default='media', upload_to='media'),
        ),
    ]
