# Generated by Django 4.1.2 on 2022-11-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_t20_t_twenty'),
    ]

    operations = [
        migrations.CreateModel(
            name='EVENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=122)),
                ('event_type', models.CharField(max_length=122)),
                ('event_format', models.CharField(max_length=122)),
                ('hosting_country', models.CharField(max_length=122)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
            ],
        ),
    ]
