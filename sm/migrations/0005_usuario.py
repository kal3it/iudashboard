# Generated by Django 2.0 on 2017-12-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm', '0004_auto_20171209_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
                ('nivel', models.IntegerField()),
            ],
        ),
    ]
