# Generated by Django 3.1 on 2022-03-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useful', models.CharField(max_length=20)),
                ('interesting_comments', models.CharField(max_length=30)),
            ],
        ),
    ]
