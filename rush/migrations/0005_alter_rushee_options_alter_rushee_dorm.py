# Generated by Django 5.0.7 on 2024-07-18 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rush', '0004_alter_rushee_options_remove_rushee_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rushee',
            options={'ordering': ['status', 'name']},
        ),
        migrations.AlterField(
            model_name='rushee',
            name='dorm',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
