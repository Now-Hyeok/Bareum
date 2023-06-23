# Generated by Django 4.2.1 on 2023-06-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]