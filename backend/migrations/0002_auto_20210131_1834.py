# Generated by Django 3.1.2 on 2021-01-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='code',
            field=models.CharField(default='0000000', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
