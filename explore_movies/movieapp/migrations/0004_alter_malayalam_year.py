# Generated by Django 4.2.2 on 2024-01-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_alter_malayalam_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malayalam',
            name='year',
            field=models.DateField(),
        ),
    ]