# Generated by Django 5.1.4 on 2025-01-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_vacancy_is_active_alter_vacancy_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]