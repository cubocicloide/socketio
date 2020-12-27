"""Socket.IO configuration with Django

This is an example of how to use python-socketio with asgi from within a Django application.
The example is inspired by https://github.com/miguelgrinberg/python-socketio/tree/master/examples/server/asgi.
An analogous example inwhich wsgi is used instead of asgi is given at https://github.com/miguelgrinberg/python-socketio/tree/master/examples/server/wsgi/django_example
"""
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.response import Response


from home.asgi import sio


class IndexView(TemplateView):
    template_name = "index.html"


@sio.event
async def my_event(sid, message):
    await sio.emit('my_response', {'data': message['data']}, room=sid)


@sio.event
async def my_broadcast_event(sid, message):
    await sio.emit('my_response', {'data': message['data']})


@sio.event
async def join(sid, message):
    sio.enter_room(sid, message['room'])
    await sio.emit('my_response', {'data': 'Entered room: ' + message['room']},
             room=sid)


@sio.event
async def leave(sid, message):
    sio.leave_room(sid, message['room'])
    await sio.emit('my_response', {'data': 'Left room: ' + message['room']},
             room=sid)


@sio.event
async def close_room(sid, message):
    await sio.emit('my_response',
             {'data': 'Room ' + message['room'] + ' is closing.'},
             room=message['room'])
    await sio.close_room(message['room'])


@sio.event
async def my_room_event(sid, message):
    await sio.emit('my_response', {'data': message['data']}, room=message['room'])


@sio.event
async def disconnect_request(sid):
    await sio.disconnect(sid)


@sio.event
async def connect(sid, environ):
    await sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)


@sio.event
async def disconnect(sid):
    print('Client disconnected')

