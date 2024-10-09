# Generated by Django 3.2.6 on 2024-10-09 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acudiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Colegio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('grado', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('jornada', models.CharField(max_length=50)),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituciones.colegio')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('acudientes', models.ManyToManyField(related_name='estudiantes', to='instituciones.Acudiente')),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituciones.colegio')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituciones.grado')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instituciones.colegio')),
            ],
        ),
    ]