# Generated by Django 4.0.4 on 2022-06-28 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_remove_coursedetail_specialization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='announcements_on_load',
            new_name='announcements_popup_on_load',
        ),
    ]