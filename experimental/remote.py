from socketIO_client import SocketIO, BaseNamespace
from threading import Thread
from time import sleep
import base64

latest_orientation={'alpha':0, 'beta':0, 'gamma':0}
latest_geolocation={}
latest_picture=None
client_id=0
io = None

class ClientsNamespace(BaseNamespace):
    def on_connect(self):
        print('connected')
    def on_identify(self, fn):
        fn(client_id);
    def on_geolocation(self, geolocation):
        global latest_geolocation 
        latest_geolocation = geolocation
    def on_orientation(self, orientation):
        global latest_orientation
        latest_orientation = orientation

def _wait(socketIO):
    socketIO.wait()

def get_geolocation():
    global latest_geolocation
    return latest_geolocation

def get_orientation():
    global latest_orientation
    return latest_orientation

def got_picture(data):
    global latest_picture
    _,b = data.split(',')
    latest_picture = base64.b64decode(b)

def get_picture():
    global latest_picture
    latest_picture = None
    io.emit("get_picture", got_picture)
    while latest_picture is None:
        sleep(0.1)
    return latest_picture


def initConnection(id=1234, url="https://127.0.0.1:3443"):
    global client_id
    global io
    client_id = id
    socketIO = SocketIO(url, verify=False)
    io = socketIO.define(ClientsNamespace, '/clients')

    thread = Thread(target=_wait, args=[socketIO])
    thread.daemon = True
    thread.start()
    sleep(1)
