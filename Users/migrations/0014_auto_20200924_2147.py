# Generated by Django 3.0.8 on 2020-09-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_auto_20200924_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='Disease',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
