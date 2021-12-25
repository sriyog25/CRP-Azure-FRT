# Generated by Django 3.0.8 on 2021-10-11 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applied_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(default='company id', help_text='*required', max_length=30)),
                ('job_id', models.CharField(default='job id', help_text='*required', max_length=30)),
                ('student_id', models.CharField(default='y1', help_text='enter username ex:y16it***', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='comp_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='*required', max_length=30)),
                ('company_name', models.CharField(help_text='*required', max_length=30)),
                ('est_year', models.CharField(help_text='*required', max_length=4)),
                ('hr_name', models.CharField(help_text='*required', max_length=30)),
                ('hr_phn', models.CharField(help_text='*required', max_length=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10)])),
                ('headquaters', models.CharField(help_text='*required', max_length=30)),
                ('about', models.CharField(help_text='*required', max_length=1000)),
                ('type', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Required. Inform a valid email address.', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='job_pos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(help_text='*required', max_length=30, unique=True)),
                ('username', models.CharField(help_text='*required', max_length=30)),
                ('company_name', models.CharField(help_text='*required', max_length=30)),
                ('designation', models.CharField(help_text='*required', max_length=30)),
                ('salary', models.IntegerField(help_text='*required')),
                ('bond_years', models.IntegerField(help_text='*required')),
                ('information_technology', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('mech', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('civil', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('eee', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('ece', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('chemical', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('cse', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='stu_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='y1', help_text='enter username ex:y16it***', max_length=9)),
                ('name', models.CharField(default='full name', help_text='*required', max_length=30)),
                ('phone_number', models.CharField(help_text='*required', max_length=10, validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('fathers_name', models.CharField(help_text='*required', max_length=30)),
                ('mothers_name', models.CharField(help_text='*required', max_length=30)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=10)),
                ('place', models.CharField(max_length=30)),
                ('branch', models.CharField(choices=[('it', 'information_technology'), ('me', 'mech'), ('ce', 'civil'), ('eee', 'eee'), ('ece', 'ece'), ('ch', 'chemical'), ('cse', 'cse')], max_length=10)),
                ('cgpa_Btech', models.FloatField(help_text='*required', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('class_10_cgpa', models.FloatField(help_text='*required', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('class_12_percentage', models.FloatField(help_text='*required', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('certifications_count', models.IntegerField()),
                ('internship', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('languages', models.CharField(help_text='*required', max_length=100)),
                ('sop', models.CharField(default='statement of purpose', help_text='*required', max_length=500)),
                ('dob', models.DateField(help_text='*format is YYYY-MM-DD')),
                ('email', models.EmailField(default='anudeep.insvirat@gmail.com', help_text='Required. Inform a valid email address.', max_length=254)),
            ],
        ),
    ]
