# Generated by Django 4.1.5 on 2023-02-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
