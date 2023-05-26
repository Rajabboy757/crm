# Generated by Django 4.1.5 on 2023-03-08 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='name')),
                ('address', models.CharField(max_length=70, verbose_name='address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='location company')),
                ('employee', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='employee')),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='LocationImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.location', verbose_name='location')),
            ],
            options={
                'verbose_name': 'Location Image',
                'verbose_name_plural': 'Location Images',
            },
        ),
    ]