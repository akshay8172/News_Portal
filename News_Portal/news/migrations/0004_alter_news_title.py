# Generated by Django 5.0.7 on 2024-10-24 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_comment_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(),
        ),
    ]
