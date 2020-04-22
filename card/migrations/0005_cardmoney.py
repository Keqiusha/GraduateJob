# Generated by Django 2.0.5 on 2020-04-14 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_auto_20200412_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardmoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_money', models.CharField(default='', max_length=32)),
                ('consume_money', models.CharField(default='', max_length=32)),
                ('consume_time', models.DateTimeField(auto_now_add=True)),
                ('cardnum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.User')),
            ],
        ),
    ]