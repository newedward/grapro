# Generated by Django 3.1.2 on 2021-01-30 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('uni', models.CharField(max_length=40)),
                ('school', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_point', models.IntegerField()),
                ('middle_point', models.IntegerField()),
                ('end_point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_tea', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_tea', serialize=False, to='backend.user')),
                ('requirement', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_stu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_stu', serialize=False, to='backend.user')),
                ('teacher_fol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_fol', to='backend.teacher')),
                ('work', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workbystu', to='backend.work')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400, null=True)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works_record', to='backend.work')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stus_recode', to='backend.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teas_record', to='backend.teacher')),
            ],
        ),
    ]