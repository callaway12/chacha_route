# Generated by Django 2.2.4 on 2019-08-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_date',
            field=models.DateField(null=True),
        ),
    ]
