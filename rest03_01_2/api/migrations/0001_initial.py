# Generated by Django 5.1.2 on 2025-01-07 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('sub1', models.IntegerField()),
                ('sub2', models.IntegerField()),
            ],
        ),
    ]
