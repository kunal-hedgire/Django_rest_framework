# Generated by Django 2.0.8 on 2018-09-17 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studdb',
            old_name='Reamrks',
            new_name='Remarks',
        ),
    ]
