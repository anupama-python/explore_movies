# Generated by Django 4.2.2 on 2024-02-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_alter_english_e_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hindi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_name', models.CharField(max_length=250)),
                ('h_director', models.CharField(max_length=250)),
                ('h_year', models.DateField()),
                ('h_image', models.ImageField(default='', upload_to='imgs/%y')),
            ],
        ),
    ]
