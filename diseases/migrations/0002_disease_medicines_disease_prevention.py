# Generated by Django 5.0.4 on 2024-11-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='medicines',
            field=models.JSONField(blank=True, default='null'),
        ),
        migrations.AddField(
            model_name='disease',
            name='prevention',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
    ]