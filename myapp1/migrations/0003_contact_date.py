# Generated by Django 3.2.20 on 2023-09-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_auto_20230922_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
    ]
