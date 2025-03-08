# Generated by Django 5.0.6 on 2025-03-05 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='folder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='home.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
