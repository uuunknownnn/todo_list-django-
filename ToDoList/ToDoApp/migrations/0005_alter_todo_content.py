# Generated by Django 4.1.5 on 2023-01-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0004_alter_todo_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
