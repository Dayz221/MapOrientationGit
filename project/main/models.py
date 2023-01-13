from django.db import models


class Sessions(models.Model):
    user_id = models.TextField("Пользователи")
    route_id = models.IntegerField("id маршрута")
    current_progress = models.IntegerField("Прогресс")
    group_name = models.TextField("Название команды")


class Cards(models.Model):
    card_id = models.TextField('Физический id карты')
    virtual_id = models.IntegerField('Виртуальный id карты')
    attached_route = models.IntegerField('id привязанного маршрута')


class Boards(models.Model):
    point_name = models.TextField("Название точки")
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")
    board_id = models.IntegerField("id платы")


class Routes(models.Model):
    points = models.TextField('Маршрут, состоящий из id плат')
    route_id = models.IntegerField('id маршрута')


class Users(models.Model):
    last_ip = models.TextField('Последний ip')
    group_name = models.TextField('Имя группы')
    latitude = models.FloatField()
    longitude = models.FloatField()
