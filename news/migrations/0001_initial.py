# Generated by Django 4.1.4 on 2023-05-15 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(db_index=True, upload_to='img/news/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=100, verbose_name='Наиминование')),
                ('content', models.TextField(max_length=1000, verbose_name='Текст')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
