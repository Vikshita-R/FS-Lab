# Generated by Django 5.0.6 on 2024-07-12 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=100)),
                ('course_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('student_sem', models.IntegerField()),
                ('enrolement', models.ManyToManyField(to='main2.course')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptopic', models.CharField(max_length=200)),
                ('planguages', models.CharField(max_length=200)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main2.student')),
            ],
        ),
    ]