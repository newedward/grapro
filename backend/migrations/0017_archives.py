# Generated by Django 3.1.2 on 2021-04-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_user_valid'),
    ]

    operations = [
        migrations.CreateModel(
            name='archives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='backend.student')),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='backend.teacher')),
            ],
        ),
    ]
