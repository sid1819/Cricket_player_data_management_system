# Generated by Django 4.1.2 on 2022-11-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='t20_ranking_allrounder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=122)),
                ('ICC_raking', models.CharField(max_length=122)),
                ('player_name', models.CharField(max_length=122)),
                ('country', models.CharField(max_length=122)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='t20_ranking_batsman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=122)),
                ('ICC_raking', models.CharField(max_length=122)),
                ('player_name', models.CharField(max_length=122)),
                ('country', models.CharField(max_length=122)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='t20_ranking_bowler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=122)),
                ('ICC_raking', models.CharField(max_length=122)),
                ('player_name', models.CharField(max_length=122)),
                ('country', models.CharField(max_length=122)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
