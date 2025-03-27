# Generated by Django 5.1.7 on 2025-03-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('pr_photo', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
    ]
