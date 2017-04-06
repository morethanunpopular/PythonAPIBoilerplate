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
    socketio.emit('task_event', {"data": currentID, "room": currentID}, room=currentID, namespace='/tasks') 
    return "hello world"

@app.task
def progessiveTaskExample():
    import time
    for x in xrange(10):
      time.sleep(2)
      currentID = current_task.request.id
      socketio = SocketIO(message_queue="redis://")
      percent = (x + 1) * 10
      string = "{0}%".format(percent)
      socketio.emit('task_event', {"data": currentID, "room": currentID, "percent": string }, room=currentID, namespace='/tasks') 
    return "progessiveTaskExample is done"
