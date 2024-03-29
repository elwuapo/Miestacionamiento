# Generated by Django 2.2.2 on 2019-06-25 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0005_auto_20190625_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contratos', models.ManyToManyField(blank=True, to='web.Contrato')),
                ('estacionamientos', models.ManyToManyField(blank=True, to='web.Estacionamiento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehiculo', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.Vehiculo')),
            ],
        ),
    ]
