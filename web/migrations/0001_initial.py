# Generated by Django 2.2.2 on 2019-06-25 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=200)),
                ('latitud', models.CharField(max_length=30)),
                ('longitud', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Estado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contrastos', models.ManyToManyField(blank=True, to='web.Contrato')),
                ('estacionamientos', models.ManyToManyField(blank=True, to='web.Estacionamiento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contrato',
            name='Estacionamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Estacionamiento'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='arrendador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrendador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL),
        ),
    ]
