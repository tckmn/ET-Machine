# Generated by Django 5.0.7 on 2024-07-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0002_alter_rushee_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autobid', models.CharField(max_length=50)),
            ],
        ),
    ]
