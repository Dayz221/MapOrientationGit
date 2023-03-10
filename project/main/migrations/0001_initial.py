# Generated by Django 4.1.4 on 2023-01-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_name', models.TextField(verbose_name='Название точки')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('board_id', models.IntegerField(verbose_name='id платы')),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.TextField(verbose_name='Физический id карты')),
                ('virtual_id', models.IntegerField(verbose_name='Виртуальный id карты')),
                ('attached_route', models.IntegerField(verbose_name='id привязанного маршрута')),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.TextField(verbose_name='Маршрут, состоящий из id плат')),
                ('route_id', models.IntegerField(verbose_name='id маршрута')),
            ],
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(verbose_name='Пользователи')),
                ('route_id', models.IntegerField(verbose_name='id маршрута')),
                ('current_progress', models.IntegerField(verbose_name='Прогресс')),
                ('group_name', models.TextField(verbose_name='Название команды')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_ip', models.TextField(verbose_name='Последний ip')),
                ('group_name', models.TextField(verbose_name='Имя группы')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
