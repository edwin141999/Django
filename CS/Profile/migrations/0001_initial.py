# Generated by Django 3.0.2 on 2020-02-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('apPaterno', models.CharField(max_length=254)),
                ('apMaterno', models.CharField(max_length=254)),
                ('edad', models.IntegerField()),
                ('ciudad', models.CharField(max_length=254)),
                ('sexo', models.CharField(max_length=254)),
                ('ocupacion', models.CharField(max_length=254)),
                ('estado', models.CharField(max_length=254)),
                ('estado_civil', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Profile',
            },
        ),
    ]
