# Generated by Django 2.1.7 on 2019-03-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='orderer',
        ),
        migrations.AddField(
            model_name='tickets',
            name='alici',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets',
            name='satilib',
            field=models.BooleanField(default=False),
        ),
    ]
