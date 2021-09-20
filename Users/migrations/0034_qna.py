# Generated by Django 3.0.8 on 2020-11-12 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0033_auto_20201111_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField(blank=True, default=None, max_length=800, null=True)),
                ('Answer', models.TextField(blank=True, default=None, max_length=800, null=True)),
                ('Is_Answered', models.BooleanField(default=False)),
                ('Made_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Questions', to=settings.AUTH_USER_MODEL)),
                ('Treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Questions', to='Users.Treatment')),
            ],
        ),
    ]
