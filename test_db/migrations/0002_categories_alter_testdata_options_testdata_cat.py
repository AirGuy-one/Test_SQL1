# Generated by Django 4.1.2 on 2022-10-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='testdata',
            options={'verbose_name': 'Запись в бд', 'verbose_name_plural': 'Записи в бд'},
        ),
        migrations.AddField(
            model_name='testdata',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='test_db.categories'),
            preserve_default=False,
        ),
    ]
