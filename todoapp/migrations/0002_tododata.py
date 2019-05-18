# Generated by Django 2.2.1 on 2019-05-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tododata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]