# Generated by Django 3.1 on 2020-09-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200913_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_url', models.TextField(default='Some string')),
                ('linkedin_url', models.TextField(default='Some string')),
                ('instagram_url', models.TextField(default='Some string')),
            ],
        ),
    ]
