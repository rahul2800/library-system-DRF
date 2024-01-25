# Generated by Django 5.0.1 on 2024-01-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('registration_id', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
