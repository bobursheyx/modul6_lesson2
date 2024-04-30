# Generated by Django 5.0.4 on 2024-04-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('make', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
    ]
