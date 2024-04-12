# Generated by Django 4.2.11 on 2024-04-12 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField()),
                ('search_period', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('name', models.TextField()),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trends.keyword')),
            ],
        ),
    ]
