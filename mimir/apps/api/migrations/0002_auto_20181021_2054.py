# Generated by Django 2.1.2 on 2018-10-21 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neuralnet',
            name='active',
        ),
        migrations.RemoveField(
            model_name='neuralnet',
            name='dataset',
        ),
    ]