# Generated by Django 3.1.3 on 2023-05-22 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_info',
            name='poster_src',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]