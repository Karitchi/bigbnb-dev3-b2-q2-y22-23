# Generated by Django 4.1.7 on 2023-04-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='unread',
            field=models.BooleanField(default=True),
        ),
    ]
