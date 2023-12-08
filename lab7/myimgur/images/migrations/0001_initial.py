# Generated by Django 4.2.7 on 2023-11-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('desc', models.CharField(max_length=512)),
                ('pub_date', models.DateTimeField()),
                ('url', models.CharField(max_length=512)),
            ],
        ),
    ]
