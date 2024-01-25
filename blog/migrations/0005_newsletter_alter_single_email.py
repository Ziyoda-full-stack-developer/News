# Generated by Django 4.2.7 on 2024-01-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='single',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
