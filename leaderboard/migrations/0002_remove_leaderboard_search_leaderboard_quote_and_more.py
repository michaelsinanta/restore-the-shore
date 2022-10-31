# Generated by Django 4.1 on 2022-10-30 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0001_initial'),
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='search',
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='quote',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='users',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='landing_page.useraccount'),
        ),
    ]
