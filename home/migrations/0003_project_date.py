# Generated by Django 3.1.2 on 2020-10-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_project_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
