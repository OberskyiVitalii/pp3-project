# Generated by Django 5.0.4 on 2024-04-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='cpu',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='gpu',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='ram',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='repairorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
        migrations.DeleteModel(
            name='SparePart',
        ),
    ]
