# Generated by Django 2.0 on 2017-12-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procesados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_interaccion', models.CharField(default=None, max_length=80)),
                ('idioma', models.CharField(default=None, max_length=80)),
                ('polaridad', models.CharField(default=None, max_length=100)),
                ('anyo', models.IntegerField(default=None)),
                ('mes_nom', models.CharField(default=None, max_length=45)),
                ('mes_num', models.IntegerField(default=None)),
                ('dia_num', models.IntegerField(default=None)),
                ('dia_sem', models.CharField(default=None, max_length=45)),
                ('hora', models.IntegerField(default=None)),
                ('minuto', models.IntegerField(default=None)),
                ('isla', models.CharField(default=None, max_length=300)),
                ('municipio', models.CharField(default=None, max_length=300)),
                ('T_mallorca', models.IntegerField(default=None)),
                ('T_menorca', models.IntegerField(default=None)),
                ('T_ibiza', models.IntegerField(default=None)),
                ('T_formentera', models.IntegerField(default=None)),
                ('T_cine', models.IntegerField(default=None)),
                ('T_playa', models.IntegerField(default=None)),
                ('T_baile', models.IntegerField(default=None)),
                ('T_teatro', models.IntegerField(default=None)),
                ('T_musica', models.IntegerField(default=None)),
                ('T_conciertos', models.IntegerField(default=None)),
                ('T_restaurantes', models.IntegerField(default=None)),
                ('T_baleares', models.IntegerField(default=None)),
                ('T_hotel', models.IntegerField(default=None)),
            ],
        ),
    ]
