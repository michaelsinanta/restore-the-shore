# Generated by Django 4.1 on 2022-10-31 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_useraccount_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(max_length=63),
        ),
    ]