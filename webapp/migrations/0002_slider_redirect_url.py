# Generated by Django 3.2 on 2021-04-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='redirect_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
