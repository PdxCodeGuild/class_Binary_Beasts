# Generated by Django 3.1.3 on 2021-01-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url_shortener',
            name='shortened_url',
            field=models.CharField(default='f', max_length=800),
        ),
    ]
