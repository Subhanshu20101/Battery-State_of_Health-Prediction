import eventlet
import socketio 


SOH = {'rpi1': 0 , 'rpi2': 0, 'rpi3': 0}

SERVER = False
CLIENT = True

def fetchSOH():
    return 1000


def client(ip):
    sio = socketio.Client()

    

    def send_sensor_readings():
        sio.emit('my_message', fetchSoH())

       
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

    sio.connect('http://' + ip + ':5000')




client(ip) # ip of node2
client(ip) # ip of node3


