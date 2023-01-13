from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from main.models import *
import json


def index(request: HttpRequest):
    if Users.objects.filter(last_ip=get_ip(request)).count() > 0:
        return render(request, 'map.html')
    return render(request, 'index.html')


def create_new_group(request: HttpRequest):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        card_id = request.POST.get('card_id')
        user_ip = get_ip(request)

        if Cards.objects.filter(virtual_id=card_id).count() == 0:
            return HttpResponse('Id такой карты не существует. Пожалуйста, проверьте id карты...')

        else:
            if Sessions.objects.filter(group_name=group_name).count() > 0:
                return HttpResponse("Группа c таким названием уже существует. Придумайте другое название...")

            card = Cards.objects.get(virtual_id=card_id)
            route_id = card.attached_route
            Sessions.objects.create(user_id=json.dumps(
                [user_ip], ensure_ascii=False), route_id=route_id, current_progress=0, group_name=group_name)
            Users.objects.create(
                last_ip=user_ip, group_name=group_name, latitude=55.689263, longitude=37.920727)

    return HttpResponse('ok')


def join_group(request: HttpRequest):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        ip = get_ip(request)

        if Sessions.objects.filter(group_name=group_name).count() != 1:
            return HttpResponse('Такой группы не существует. Пожалуйста, проверьте название комады...')

        else:
            session = Sessions.objects.get(group_name=group_name)
            users = json.loads(session.user_id)
            users.append(ip)
            session.user_id = json.dumps(users)
            session.save()
            Users.objects.create(last_ip=ip, group_name=group_name)

    return HttpResponse('ok')


def exit_session(request: HttpRequest):
    ip = get_ip(request)

    if Users.objects.filter(last_ip=ip).count() == 0:
        return HttpResponse('error')
    user = Users.objects.get(last_ip=ip)

    if Sessions.objects.filter(group_name=user.group_name).count() == 0:
        return HttpResponse('error')
    session = Sessions.objects.get(group_name=user.group_name)

    users = json.loads(session.user_id)
    users.pop(users.index(ip))
    session.user_id = json.dumps(users)
    session.save()

    if session.user_id == '[]':
        session.delete()

    user.delete()

    return HttpResponse('ok')


def update(request: HttpRequest):
    ip = get_ip(request)

    try:
        user = Users.objects.get(last_ip=ip)
        session = Sessions.objects.get(group_name=user.group_name)
        route = Routes.objects.get(route_id=session.route_id)
        points = json.loads(route.points)
        cur_point = points[session.current_progress]
        board = Boards.objects.get(board_id=cur_point)
        response = {
            "point_name": board.point_name,
            "latitude": board.latitude,
            "longitude": board.longitude
        }
        return HttpResponse(json.dumps(response))

    except:
        return HttpResponse('error')


def set_position(request: HttpRequest):
    ip = get_ip(request)
    user = Users.objects.get(last_ip=ip)
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        user.latitude = latitude
        user.longitude = longitude
        user.save()

    return HttpResponse('ok')


def get_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
