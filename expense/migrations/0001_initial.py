# Generated by Django 3.0.4 on 2020-05-11 10:44

from django.db import migrations, models
import expense.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.CharField(default=expense.models.Expense.random_id, max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('actors', models.CharField(max_length=300)),
                ('dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
