# Generated by Django 4.2.7 on 2023-12-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_retails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashion',
            name='Date_Purchase',
            field=models.DateField(null=True),
        ),
    ]