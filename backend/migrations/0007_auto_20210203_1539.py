# Generated by Django 3.1.2 on 2021-02-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20210202_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='queue',
            field=models.TextField(null=True),
        ),
    ]