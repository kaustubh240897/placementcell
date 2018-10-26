# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-26 15:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0007_course1_sem1_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course2_sem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30, null=True)),
                ('file_pdfs', models.FileField(null=True, upload_to='')),
                ('video_link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Semester_1')),
            ],
        ),
        migrations.CreateModel(
            name='Course3_sem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30, null=True)),
                ('file_pdfs', models.FileField(null=True, upload_to='')),
                ('video_link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Semester_1')),
            ],
        ),
        migrations.CreateModel(
            name='Course4_sem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30, null=True)),
                ('file_pdfs', models.FileField(null=True, upload_to='')),
                ('video_link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Semester_1')),
            ],
        ),
        migrations.CreateModel(
            name='Course5_sem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30, null=True)),
                ('file_pdfs', models.FileField(null=True, upload_to='')),
                ('video_link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Semester_1')),
            ],
        ),
    ]
