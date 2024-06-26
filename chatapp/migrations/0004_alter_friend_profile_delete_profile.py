# Generated by Django 5.0.3 on 2024-03-29 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('chatapp', '0003_alter_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
