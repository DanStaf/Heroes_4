# Generated by Django 4.2 on 2024-09-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_rename_team_herostatus_rename_program_parentstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='parents',
            field=models.ManyToManyField(to='heroes.parent', verbose_name='Родители'),
        ),
    ]
