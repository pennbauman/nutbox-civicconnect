# Generated by Django 3.1.1 on 2020-11-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0007_auto_20201105_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.AddField(
            model_name='client',
            name='State',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
