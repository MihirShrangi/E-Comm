# Generated by Django 4.1.4 on 2023-08-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_complaints_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='compdesc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='compdt',
            field=models.DateField(null=True),
        ),
    ]
