# Generated by Django 4.0.4 on 2022-04-29 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio',
            new_name='portfolio_site',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='picture',
            new_name='profile_pic',
        ),
    ]
