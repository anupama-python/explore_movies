# Generated by Django 4.2.2 on 2024-01-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_alter_malayalam_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malayalam',
            name='year',
            field=models.DateTimeField(),
        ),
    ]
