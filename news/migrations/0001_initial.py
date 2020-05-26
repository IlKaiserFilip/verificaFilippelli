# Generated by Django 3.0.5 on 2020-05-26 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Giornalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Giornalista',
                'verbose_name_plural': 'Giornalisti',
            },
        ),
        migrations.CreateModel(
            name='Articolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('contenuto', models.TextField()),
                ('giornalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articoli', to='news.Giornalista')),
            ],
            options={
                'verbose_name': 'Articolo',
                'verbose_name_plural': 'Articoli',
            },
        ),
    ]
