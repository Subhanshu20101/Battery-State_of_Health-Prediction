import eventlet
import socketio

SOH = {'rpi1': 0 , 'rpi2': 0, 'rpi3': 0}

SERVER = False
CLIENT = False

def fetchSOH():
    return 1000

def compareSOH():
    # sorted_value_index = np.argsort(SOH.values())
    SOH['rpi1']= fetchSOH
    dictionary_keys = list(SOH.keys())
    SOH = {dictionary_keys[i]: sorted(SOH.values())[i] for i in range(len(dictionary_keys))}


    # if SOH['soh1'] > SOH['soh2']:
    #     if SOH['soh1'] >= SOH['soh3']:
    #         pass
    #     if 

def server():
    sio = socketio.Server()
    app = socketio.WSGIApp(sio)

    @sio.event
    def connect(sid, environ):
        print('connect ', sid)
        # sio.start_background_task

    @sio.event
    def rpi2(sid, data):
        SOH['rpi2']=data
        # print('message ', data)
    
    @sio.event
    def rpi3(sid, data):
        SOH['rpi3']=data
        # print('message ', data)

    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)

    # if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)



def client():
    sio = socketio.Client()

    

    def send_sensor_readings():
        while True:
            sio.emit('rpi1', {'SoH': fetchSOH()})
            sio.sleep(5)

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




while True:
    if SERVER == True:
        server()

    if CLIENT == True:
        client()
        