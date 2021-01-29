#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect

"""
Clas Representing the /tasks name space
"""
class tasks(Namespace):
     
    """ Handler function for room subscription """
    def on_room_subscribe_event(self, message):
        # Actually process the join event
        join_room(message['room'])
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('room_subscribe_event_callback', 
           {'data': 'Joined successfully', 'room': message['room']}) 

    def on_task_event(self, message):
      print("task_event received")

    def on_connect(self):
        emit('connect_callback', {'data': 'Connected', 'count': 0})

    def on_disconnect(self):
        print('Client disconnected', request.sid)
