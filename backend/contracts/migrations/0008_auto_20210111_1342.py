# Generated by Django 3.0.7 on 2021-01-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0007_auto_20210111_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractdetail',
            name='value',
            field=models.FloatField(),
        ),
    ]