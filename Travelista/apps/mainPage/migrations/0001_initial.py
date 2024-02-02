# Generated by Django 4.2.9 on 2024-02-02 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, validators=[django.core.validators.MaxLengthValidator], verbose_name='Full Name')),
                ('email', models.EmailField(max_length=255, validators=[django.core.validators.EmailValidator], verbose_name='Email Address')),
                ('subject', models.CharField(blank=True, max_length=255, validators=[django.core.validators.MaxLengthValidator], verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message Text')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-created_date',),
            },
        ),
    ]
