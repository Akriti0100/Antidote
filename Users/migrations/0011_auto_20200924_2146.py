# Generated by Django 3.0.8 on 2020-09-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_treatment_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='Disease',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
