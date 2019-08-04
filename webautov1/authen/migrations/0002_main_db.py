# Generated by Django 2.0.5 on 2019-03-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='main_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('messages', models.CharField(default='', max_length=100000)),
                ('current', models.CharField(max_length=1000)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
