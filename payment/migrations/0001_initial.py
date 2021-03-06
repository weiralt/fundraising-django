# Generated by Django 3.2.5 on 2021-11-27 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0018_auto_20211127_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_order_no', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('paid_date', models.DateTimeField()),
                ('expired_date', models.DateTimeField()),
                ('bank_code', models.CharField(max_length=10)),
                ('code_no', models.CharField(max_length=50)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('pledge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='project.pledge')),
            ],
        ),
    ]
