import celery import Celery, states, Task

#define celery app
app = Celery('tasks', broker='mongodb://localhost:27017/silon', backend="mongodb://localhost:27017/silon")


# Simple "hello world" task
@app.task
def helloWorld():
    import time
    time.sleep(15)
    return "hello world"


