# Generated by Django 3.2.5 on 2021-07-22 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todays',
            fields=[
                ('category', models.CharField(max_length=700)),
                ('brand', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('today', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'todays',
            },
        ),
    ]
