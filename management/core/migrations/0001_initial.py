# Generated by Django 3.1.2 on 2022-01-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('school_name', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('school_address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
