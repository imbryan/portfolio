# Generated by Django 5.0.4 on 2024-09-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_blogpost_updated_project_project_board_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_role',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]