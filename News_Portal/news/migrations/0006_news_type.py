# Generated by Django 5.1.2 on 2024-10-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='type',
            field=models.CharField(default='kerala', max_length=20),
            preserve_default=False,
        ),
    ]
