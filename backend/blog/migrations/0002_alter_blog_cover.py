# Generated by Django 4.2.7 on 2023-12-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/blog'),
        ),
    ]
