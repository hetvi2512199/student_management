# Generated by Django 3.1.2 on 2022-01-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_subject_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
