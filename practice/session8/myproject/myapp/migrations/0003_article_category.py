# Generated by Django 4.1.7 on 2023-03-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_name_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
