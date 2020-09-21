# Generated by Django 3.1 on 2020-09-04 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_content', models.TextField(default='Some string')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_summary', models.TextField(default='Some string')),
                ('project_technologies', models.TextField(default='Some string')),
            ],
        ),
        migrations.DeleteModel(
            name='Segment',
        ),
    ]