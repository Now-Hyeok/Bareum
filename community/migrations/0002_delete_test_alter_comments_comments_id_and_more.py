# Generated by Django 4.2.1 on 2023-06-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("community", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="test",
        ),
        migrations.AlterField(
            model_name="comments",
            name="comments_id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="post_id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]