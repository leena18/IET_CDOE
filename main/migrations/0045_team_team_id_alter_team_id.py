# Generated by Django 4.0.6 on 2022-07-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]