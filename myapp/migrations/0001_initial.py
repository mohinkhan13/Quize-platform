# Generated by Django 5.1.2 on 2024-10-17 04:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('is_login', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=100)),
                ('exam_subject', models.CharField(max_length=100)),
                ('exam_type', models.CharField(choices=[('MCQ', 'Multiple Choice Questions'), ('TF', 'True/False'), ('SA', 'Short Answer'), ('MX', 'Mix')], max_length=80)),
                ('number_of_questions', models.PositiveBigIntegerField()),
                ('time_setting', models.CharField(choices=[('exam', 'Full Exam Time'), ('question', 'Single Question Time')], max_length=50)),
                ('exam_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customuser')),
            ],
        ),
    ]
