# Generated by Django 4.1.7 on 2023-03-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('parol', models.CharField(max_length=255)),
                ('manzil', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('viza', models.FileField(blank=True, null=True, upload_to='')),
                ('passport', models.FileField(blank=True, null=True, upload_to='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
