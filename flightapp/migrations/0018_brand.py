# Generated by Django 3.2.12 on 2022-08-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0017_featurerights_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
