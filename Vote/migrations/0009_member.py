# Generated by Django 2.2.18 on 2021-02-16 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vote', '0008_auto_20210211_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
