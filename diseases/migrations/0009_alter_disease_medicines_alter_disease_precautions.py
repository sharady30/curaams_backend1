# Generated by Django 5.0.4 on 2024-11-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0008_rename_prevention_disease_precautions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='medicines',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='disease',
            name='precautions',
            field=models.JSONField(),
        ),
    ]
