# Generated by Django 3.2.7 on 2022-02-16 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_poem_paragraths'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='paragraths',
            new_name='paragraphs',
        ),
    ]