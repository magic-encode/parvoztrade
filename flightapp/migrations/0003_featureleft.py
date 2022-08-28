# Generated by Django 3.2.12 on 2022-08-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightapp', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureLeft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('price_old', models.FloatField(verbose_name='mahsulotning eski narxi')),
                ('price_new', models.FloatField(verbose_name='mahsulotning yangi narxi')),
            ],
        ),
    ]
