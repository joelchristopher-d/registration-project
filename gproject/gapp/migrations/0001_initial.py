# Generated by Django 4.1.7 on 2023-02-22 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=100, unique=True)),
                ('dob', models.DateField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('private', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
                ('ed1_quali', models.CharField(max_length=100)),
                ('ed1_year', models.CharField(max_length=100)),
                ('ed1_percent', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employeer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('aadhar', models.CharField(blank=True, max_length=100, unique=True)),
                ('dob', models.DateField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('private', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=100)),
                ('ed1_quali', models.CharField(max_length=100)),
                ('ed1_year', models.CharField(max_length=100)),
                ('ed1_percent', models.CharField(max_length=100)),
            ],
        ),
    ]
