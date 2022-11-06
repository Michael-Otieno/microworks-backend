# Generated by Django 4.1.3 on 2022-11-04 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('machine_id', models.CharField(max_length=255)),
                ('availability', models.TextField()),
                ('time_in', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['full_name'],
            },
        ),
    ]