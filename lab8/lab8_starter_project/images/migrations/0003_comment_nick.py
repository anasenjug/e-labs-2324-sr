# Generated by Django 4.1.4 on 2022-12-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='nick',
            field=models.CharField(default='anon', max_length=128),
        ),
    ]
