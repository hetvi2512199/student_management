# Generated by Django 3.1.2 on 2022-01-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220126_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
