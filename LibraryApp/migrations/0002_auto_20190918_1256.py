# Generated by Django 2.2.5 on 2019-09-18 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Fine',
            new_name='fine',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='StudentClass',
            new_name='studclass',
        ),
    ]