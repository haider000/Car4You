# Generated by Django 2.1.3 on 2019-01-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=50)),
                ('user_mobile', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
