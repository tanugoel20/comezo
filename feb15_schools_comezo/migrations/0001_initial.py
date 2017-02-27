# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 22:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=200)),
                ('section_id', models.CharField(max_length=200)),
                ('days_present', models.IntegerField(null=True)),
                ('days_absent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='exam_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=200)),
                ('exam_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='marksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=200)),
                ('section_id', models.CharField(max_length=200)),
                ('subject_marks', models.CharField(max_length=200)),
                ('exam_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='school_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.CharField(max_length=200, unique=True)),
                ('school_name', models.CharField(max_length=200)),
                ('affiliation', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('start_class', models.CharField(max_length=200)),
                ('end_class', models.CharField(max_length=200)),
                ('section_class1', models.IntegerField(null=True)),
                ('section_class2', models.IntegerField(null=True)),
                ('section_class3', models.IntegerField(null=True)),
                ('section_class4', models.IntegerField(null=True)),
                ('section_class5', models.IntegerField(null=True)),
                ('section_class6', models.IntegerField(null=True)),
                ('section_class7', models.IntegerField(null=True)),
                ('section_class8', models.IntegerField(null=True)),
                ('section_class9', models.IntegerField(null=True)),
                ('section_class10', models.IntegerField(null=True)),
                ('section_class11', models.IntegerField(null=True)),
                ('section_class12', models.IntegerField(null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('roll_number', models.IntegerField(null=True)),
                ('class_id', models.CharField(max_length=200)),
                ('section_id', models.CharField(max_length=200)),
                ('admission_no', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('doj', models.CharField(max_length=200)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_contact', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info')),
            ],
        ),
        migrations.CreateModel(
            name='subject_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=200)),
                ('section_id', models.CharField(max_length=200)),
                ('subject_name', models.CharField(max_length=200)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info')),
            ],
        ),
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='teacher_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info')),
            ],
        ),
        migrations.CreateModel(
            name='teacher_subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=200)),
                ('section_id', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.teacher_info')),
            ],
        ),
        migrations.AddField(
            model_name='subject_class',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.subjects'),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info'),
        ),
        migrations.AddField(
            model_name='marksheet',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.student_info'),
        ),
        migrations.AddField(
            model_name='exam_class',
            name='exam_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.exams'),
        ),
        migrations.AddField(
            model_name='exam_class',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='school_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.school_info'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feb15_schools_comezo.student_info'),
        ),
    ]
