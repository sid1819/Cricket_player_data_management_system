# Generated by Django 4.1.2 on 2022-11-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MATCHE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_type', models.CharField(max_length=122)),
                ('venue', models.CharField(max_length=122)),
                ('team1', models.CharField(max_length=122)),
                ('team2', models.CharField(max_length=122)),
                ('date', models.DateField()),
                ('winner', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='ONEDAY',
            fields=[
                ('playerID', models.CharField(max_length=122, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=122)),
                ('debut', models.DateField()),
                ('country', models.CharField(max_length=122)),
                ('matches', models.IntegerField()),
                ('run', models.IntegerField()),
                ('fifty', models.IntegerField()),
                ('hundread', models.IntegerField()),
                ('average', models.FloatField()),
                ('strike_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PLAYER',
            fields=[
                ('playerID', models.CharField(max_length=122, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=122)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='T20',
            fields=[
                ('playerID', models.CharField(max_length=122, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=122)),
                ('debut', models.DateField()),
                ('country', models.CharField(max_length=122)),
                ('matches', models.IntegerField()),
                ('run', models.IntegerField()),
                ('fifty', models.IntegerField()),
                ('hundread', models.IntegerField()),
                ('average', models.FloatField()),
                ('strike_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TEST',
            fields=[
                ('playerID', models.CharField(max_length=122, primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=122)),
                ('debut', models.DateField()),
                ('country', models.CharField(default='country', max_length=122)),
                ('matches', models.IntegerField()),
                ('run', models.IntegerField()),
                ('fifty', models.IntegerField()),
                ('century', models.IntegerField()),
                ('double_century', models.IntegerField()),
                ('average', models.FloatField()),
                ('strike_rate', models.FloatField()),
            ],
        ),
    ]
