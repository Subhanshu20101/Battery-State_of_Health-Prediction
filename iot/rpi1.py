import socketio

sio = socketio.Client()
# print(sio.sid)

def fetchSOH():
    return 1000

def send_sensor_readings():
    
    sio.emit('my_message', fetchSOH())
    
    # while True:
    #     sio.emit('my_message', fetchSOH())
    #     sio.sleep(5)

@sio.event
def connect():
    print('connection established')
    sio.start_background_task(send_sensor_readings)
    # sio.disconnect()  


# @sio.event
# def my_message(data):
#     print('message received with ', data)
    # sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://172.16.142.222:5000')
