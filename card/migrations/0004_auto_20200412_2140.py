# Generated by Django 2.0.5 on 2020-04-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_user_onlyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
