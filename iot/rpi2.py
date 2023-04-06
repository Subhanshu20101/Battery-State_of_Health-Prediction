import socketio

sio = socketio.Client()

def fetchSOH():
    return 800


def send_sensor_readings():
    while True:
        sio.emit('my_message', fetchSOH())
        sio.sleep(10)

@sio.event
def connect():
    print('connection established')
    sio.start_background_task(send_sensor_readings)





# @sio.event
# def my_message(data):
#     print('message received with ', data)
#     sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://172.16.84.83:5000')
    