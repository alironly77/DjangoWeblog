# Generated by Django 3.2.15 on 2022-08-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_app', '0002_alter_articles_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
