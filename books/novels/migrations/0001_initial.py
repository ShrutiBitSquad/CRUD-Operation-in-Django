# Generated by Django 4.1.5 on 2023-01-31 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nName', models.CharField(max_length=50)),
                ('nAuthor', models.CharField(max_length=50)),
                ('nPublish', models.DateField()),
            ],
        ),
    ]
