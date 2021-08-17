# Generated by Django 3.2.6 on 2021-08-17 10:16

import chat.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(db_index=True, max_length=64, verbose_name='Автор')),
                ('email', models.EmailField(max_length=64, validators=[chat.custom_validators.validate_email], verbose_name='Емейл')),
                ('text', models.CharField(max_length=100, validators=[chat.custom_validators.validate_message], verbose_name='Текст сообщения')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
            ],
        ),
    ]