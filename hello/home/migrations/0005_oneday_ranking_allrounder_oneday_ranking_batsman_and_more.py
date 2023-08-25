# Generated by Django 4.1.2 on 2022-11-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_t20_ranking_allrounder_t20_ranking_batsman_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='oneday_ranking_allrounder',
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
            name='oneday_ranking_batsman',
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
            name='oneday_ranking_bowler',
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
            name='test_ranking_batsman',
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
            name='test_ranking_bowler',
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
