# Generated by Django 3.2 on 2021-08-06 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='firstname',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lastname',
            new_name='lastName',
        ),
    ]