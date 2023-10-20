# Generated by Django 3.2.7 on 2022-03-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0002_auto_20220329_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='multichoicequestion',
            name='multipleAnswers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='numberscalequestion',
            name='maxTitleOn',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='numberscalequestion',
            name='midTitleOn',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='numberscalequestion',
            name='minTitleOn',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='numberscalequestion',
            name='interval',
            field=models.IntegerField(default=1),
        ),
    ]
