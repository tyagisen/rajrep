# Generated by Django 3.2.9 on 2021-11-23 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='jobapp.job'),
        ),
    ]
