# Generated by Django 3.2.7 on 2022-04-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveytaker', '0003_auto_20220407_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='respondent_identifier',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
