# Generated by Django 3.1.2 on 2022-01-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_student_enrollment_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_code', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
