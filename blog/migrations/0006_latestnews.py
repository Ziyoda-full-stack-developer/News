# Generated by Django 4.2.7 on 2024-01-05 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_newsletter_alter_single_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('img', models.ImageField(upload_to='latestNews/')),
                ('status', models.CharField(max_length=99)),
                ('bio', models.CharField(max_length=100)),
            ],
        ),
    ]
