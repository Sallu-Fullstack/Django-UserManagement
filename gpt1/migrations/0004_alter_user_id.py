# Generated by Django 4.1.7 on 2023-03-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt1', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
