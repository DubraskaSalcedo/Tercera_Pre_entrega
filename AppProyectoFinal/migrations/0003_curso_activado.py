# Generated by Django 4.1.7 on 2023-03-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinal', '0002_alter_estudiante_email_alter_profesor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='activado',
            field=models.BooleanField(default=False),
        ),
    ]
