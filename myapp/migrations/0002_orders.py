# Generated by Django 4.1.4 on 2023-08-07 11:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orddt', models.DateField(default=datetime.date.today)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.usermaster')),
            ],
        ),
    ]
