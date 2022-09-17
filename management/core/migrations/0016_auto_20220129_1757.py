# Generated by Django 3.1.2 on 2022-01-29 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_course_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.standard'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(blank=True, null=True, to='core.Subject'),
        ),
    ]
