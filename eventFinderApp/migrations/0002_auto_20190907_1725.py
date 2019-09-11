# Generated by Django 2.2 on 2019-09-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ManyToManyField(to='eventFinderApp.Category'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
