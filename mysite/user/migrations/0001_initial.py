# Generated by Django 4.1 on 2022-09-06 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('token', models.CharField(blank=True, max_length=64, null=True, verbose_name='TOKEN')),
            ],
            options={
                'db_table': 'db_user',
            },
        ),
    ]
