# Generated by Django 4.1.5 on 2023-01-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appp1', '0002_boxdetails_additional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxdetails',
            name='additional',
            field=models.TextField(blank=True, null=True),
        ),
    ]