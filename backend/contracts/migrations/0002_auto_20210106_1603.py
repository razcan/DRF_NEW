# Generated by Django 3.0.7 on 2021-01-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='approved_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='dimm_4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='status_id',
            field=models.IntegerField(default=1),
        ),
    ]