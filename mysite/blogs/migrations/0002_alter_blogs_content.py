# Generated by Django 4.1 on 2022-09-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.TextField(),
        ),
    ]
