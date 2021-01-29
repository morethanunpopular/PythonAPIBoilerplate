from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect
import eventlet
import pkgutil
import namespaces 

# Apply eventlet's monkey patch
eventlet.monkey_patch()

# Define App configureation
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet', message_queue='redis://')

# Define name spaces
nameSpaces = [name for _, name, _ in pkgutil.iter_modules(['namespaces'])]
for namespace in nameSpaces:
  importString = "{0}.{1}".format('namespaces', namespace)
  namespaceModule = __import__(importString, globals(), locals(), [namespace], 0) 
  socketio.on_namespace(namespaceModule.__dict__[namespace]('/{0}'.format(namespace)))

# Define route for serving test client
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

if __name__ == '__main__':
    socketio.run(app, debug=True)
