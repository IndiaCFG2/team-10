# Generated by Django 3.0.3 on 2020-08-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200809_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video_link',
            field=models.CharField(default='', max_length=100),
        ),
    ]
