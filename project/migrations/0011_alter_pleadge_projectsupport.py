# Generated by Django 3.2.5 on 2021-11-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pleadge',
            name='projectsupport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pleadge', to='project.projectsupport'),
        ),
    ]
