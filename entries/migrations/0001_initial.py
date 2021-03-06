# Generated by Django 3.2.1 on 2021-11-14 01:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('prep_time', models.CharField(max_length=200)),
                ('cook_time', models.CharField(max_length=200)),
                ('serves', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.localtime)),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
        ),
    ]
