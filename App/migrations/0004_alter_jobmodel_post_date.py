# Generated by Django 5.1.1 on 2024-09-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_applynowmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='post_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]