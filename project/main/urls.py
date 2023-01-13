from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_new_group', views.create_new_group),
    path('join_group', views.join_group),
    path('exit_session', views.exit_session),
    path('update', views.update),
    path('set_position', views.set_position),
]
