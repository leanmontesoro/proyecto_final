# Generated by Django 4.1.3 on 2022-12-30 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMain', '0005_entrada_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='read_time',
            field=models.CharField(default='No especificado', max_length=50),
        ),
    ]
