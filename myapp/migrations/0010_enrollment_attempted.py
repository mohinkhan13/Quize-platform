# Generated by Django 5.1.2 on 2024-10-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_exam_difficulty_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='attempted',
            field=models.IntegerField(default=0),
        ),
    ]