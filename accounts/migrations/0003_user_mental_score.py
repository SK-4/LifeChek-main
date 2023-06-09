# Generated by Django 4.1.7 on 2023-03-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mental_score',
            field=models.DecimalField(blank=True, decimal_places=2, error_messages={'max_value': "Mental score can't be greater than 100%", 'min_value': "Mental score can't be less than 0%"}, max_digits=5, null=True),
        ),
    ]
