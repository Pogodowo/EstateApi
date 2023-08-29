# Generated by Django 4.1.5 on 2023-08-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='baza_ogloszen',
            fields=[
                ('tytul', models.CharField(blank=True, max_length=80, null=True)),
                ('lokalizacja', models.CharField(blank=True, max_length=80, null=True)),
                ('cena', models.CharField(blank=True, max_length=30, null=True)),
                ('cena_za_metr', models.CharField(blank=True, max_length=30, null=True)),
                ('liczba_pokoi', models.CharField(blank=True, max_length=30, null=True)),
                ('powierzchnia', models.CharField(blank=True, max_length=20, null=True)),
                ('url_link', models.TextField(blank=True, max_length=200, null=True)),
                ('foto', models.TextField(blank=True, max_length=300, null=True)),
                ('data_wystawienia', models.DateTimeField(blank=True, null=True)),
                ('data_zakonczenia', models.DateTimeField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ulubione', models.CharField(blank=True, default='off', max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='linki_otodom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul_linka', models.CharField(blank=True, max_length=80, null=True)),
                ('url_linka', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='test_aktywnosci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_skryptu', models.CharField(blank=True, max_length=20, null=True)),
                ('aktywnosc_skryptu', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
