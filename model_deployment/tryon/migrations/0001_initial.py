# Generated by Django 3.1.6 on 2021-02-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tryon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pose', models.ImageField(upload_to='model/input/image')),
                ('cloth', models.ImageField(upload_to='model/input/cloth')),
            ],
        ),
    ]
