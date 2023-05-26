# Generated by Django 4.1.5 on 2023-03-08 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='logo')),
                ('employee', models.ManyToManyField(related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='employee')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_owner', to=settings.AUTH_USER_MODEL, verbose_name='company_owner')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='product name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='price')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('count', models.IntegerField(verbose_name='count')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.company', verbose_name='company')),
            ],
        ),
    ]