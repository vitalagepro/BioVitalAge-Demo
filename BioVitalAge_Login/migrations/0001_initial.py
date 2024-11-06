# Generated by Django 5.1.1 on 2024-11-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utenti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('data_registrazione', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Utenti',
            },
        ),
    ]