import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio)
# print(sio.sid)

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    # sio.start_background_task

@sio.event
def my_message(sid, data):
    print('message ', data)
    # sio.emit('my_message', 'owerhf')
    sio.disconnect(sid)
    eventlet.greenthread.kill(app)
    # return

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)