# Generated by Django 3.1.1 on 2020-11-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0014_auto_20201108_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='representatives',
        ),
        migrations.AddField(
            model_name='client',
            name='representatives',
            field=models.ManyToManyField(to='masterdata.Representative'),
        ),
    ]
