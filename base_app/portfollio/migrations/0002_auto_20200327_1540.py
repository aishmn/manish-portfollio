# Generated by Django 3.0.4 on 2020-03-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfollio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfollio',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
