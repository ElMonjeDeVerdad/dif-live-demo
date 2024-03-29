# Generated by Django 3.0.2 on 2020-06-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200606_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerta',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='alerta',
            name='riesgo',
            field=models.CharField(choices=[('3', '3'), ('2', '2'), ('1', '1')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alerta',
            name='tipo',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alerta',
            name='mensaje',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
