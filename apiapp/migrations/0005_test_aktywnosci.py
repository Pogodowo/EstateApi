# Generated by Django 4.1.5 on 2023-03-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0004_linki_otodom'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_aktywnosci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_wystawienia', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]