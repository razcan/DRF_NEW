# Generated by Django 3.0.7 on 2021-01-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20210106_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='dimm_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_4',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
