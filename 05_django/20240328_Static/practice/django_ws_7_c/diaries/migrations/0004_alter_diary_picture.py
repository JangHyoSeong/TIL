# Generated by Django 4.2.9 on 2024-03-28 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0003_alter_diary_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='picture',
            field=models.ImageField(blank=True, upload_to='%Y/%b/%a'),
        ),
    ]
