# Generated by Django 5.0.2 on 2024-03-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_alter_habilidades_options_alter_empleado_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombres completos'),
        ),
    ]
