# Generated by Django 4.1.2 on 2022-11-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_db', '0005_alter_testdatarelation_options_testdatarelation_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdatarelation',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'fine'), (2, 'good'), (3, 'amazing')]),
        ),
    ]