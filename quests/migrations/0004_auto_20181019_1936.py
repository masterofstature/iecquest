# Generated by Django 2.1.2 on 2018-10-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0003_auto_20181019_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelvisual',
            name='position',
            field=models.CharField(default='0 0 0', max_length=50),
        ),
        migrations.AddField(
            model_name='modelvisual',
            name='rotation',
            field=models.CharField(default='0 0 0', max_length=50),
        ),
    ]