# Generated by Django 3.1.3 on 2020-11-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201111_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
