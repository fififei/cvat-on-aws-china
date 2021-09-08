# Generated by Django 3.2.6 on 2021-08-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('spec', models.CharField(max_length=5000)),
                ('framework', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('help_message', models.CharField(max_length=100)),
                ('animated_gif', models.CharField(max_length=100)),
                ('min_pos_points', models.IntegerField(default=1)),
                ('min_neg_points', models.IntegerField(default=-1)),
                ('startswith_box', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
