# Generated by Django 3.2.5 on 2021-11-19 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_pleadge_projectsupport'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='donate',
            field=models.IntegerField(default=0),
        ),
    ]
