# Generated by Django 4.2.1 on 2023-06-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_first_name_remove_user_last_name'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='login_id',
            field=models.CharField(max_length=150, unique=True, verbose_name='login ID'),
        ),
    ]