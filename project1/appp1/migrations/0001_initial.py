# Generated by Django 4.1.5 on 2023-01-28 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoxDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('qbox_no', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('password', models.CharField(blank=True, max_length=70, null=True)),
                ('source', models.CharField(max_length=70)),
                ('teleport', models.CharField(blank=True, max_length=70, null=True)),
                ('sudo_password', models.CharField(blank=True, max_length=70, null=True)),
                ('apihub', models.CharField(blank=True, max_length=70, null=True)),
                ('web_frontend', models.CharField(blank=True, max_length=70, null=True)),
                ('checkpoints', models.CharField(blank=True, max_length=70, null=True)),
                ('cxr_api', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]
