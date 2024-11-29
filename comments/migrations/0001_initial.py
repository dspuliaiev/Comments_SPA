# Generated by Django 5.1.3 on 2024-11-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название файла')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Файл')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
            ],
        ),
    ]