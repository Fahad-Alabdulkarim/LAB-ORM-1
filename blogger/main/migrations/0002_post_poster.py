# Generated by Django 5.1.2 on 2024-11-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
