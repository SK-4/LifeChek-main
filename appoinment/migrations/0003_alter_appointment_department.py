# Generated by Django 4.1.7 on 2023-03-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoinment', '0002_takeappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='department',
            field=models.CharField(choices=[('Psychologist', 'Psychologist'), ('Physiotherapist', 'Physiotherapist')], max_length=100),
        ),
    ]
