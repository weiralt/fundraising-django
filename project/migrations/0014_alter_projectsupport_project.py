# Generated by Django 3.2.5 on 2021-11-19 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20211119_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsupport',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='projectsupports', to='project.project'),
        ),
    ]