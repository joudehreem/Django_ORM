# Generated by Django 5.0.7 on 2024-07-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
