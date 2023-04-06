import eventlet
import socketio 

SOH = {'rpi1': 0 , 'rpi2': 0, 'rpi3': 0}

SERVER = True
CLIENT = False

def fetchSOH():
    return 800


def server():
    sio = socketio.Server()
    app = socketio.WSGIApp(sio)

    @sio.event
    def connect(sid, environ):
        print('connect ', sid)
        

    @sio.event
    def my_message(sid, data):
        SOH['rpi2']=data
        sio.disconnect(sid)
        # print('message ', data)
    
    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)

    # if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)



server()
