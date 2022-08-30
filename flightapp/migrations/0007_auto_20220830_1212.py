# Generated by Django 3.2.12 on 2022-08-30 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flightapp', '0006_auto_20220830_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='image',
        ),
        migrations.CreateModel(
            name='SubComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='foydalanuvchilar', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentlar', to='flightapp.products')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightapp.comments')),
            ],
        ),
    ]
