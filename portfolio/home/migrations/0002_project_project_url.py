# Generated by Django 3.0.3 on 2020-02-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
    ]