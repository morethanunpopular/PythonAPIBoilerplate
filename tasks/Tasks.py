from celery import Celery, states, Task

#define celery app
app = Celery('tasks', broker='mongodb://localhost:27017/app', backend="mongodb://localhost:27017/app")


# Simple "hello world" task
@app.task
def helloWorld():
    import time
    time.sleep(15)
    return "hello world"


