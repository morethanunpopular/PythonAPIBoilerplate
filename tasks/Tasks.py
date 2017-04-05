from celery import Celery, states, Task, current_task
from flask_socketio import SocketIO
#define celery app
app = Celery('tasks', broker='mongodb://localhost:27017/app', backend="mongodb://localhost:27017/app")


# Simple "hello world" task
@app.task
def helloWorld():
    import time
    time.sleep(20)
    currentID = current_task.request.id
    socketio = SocketIO(message_queue="redis://")
    socketio.emit('my_response', {"data": currentID, "room": currentID}, room=currentID, namespace='/test') 
    return "hello world"


