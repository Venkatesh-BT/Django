# Generated by Django 3.0.2 on 2020-02-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('jersy_num', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'player',
                'verbose_name_plural': 'players',
            },
        ),
    ]