# Generated by Django 4.2.1 on 2023-08-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('formed_year', models.PositiveIntegerField()),
                ('members', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]