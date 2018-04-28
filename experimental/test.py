from time import sleep
from remote import initConnection, get_geolocation, get_orientation 

initConnection(id=1235)
while True:
    print(get_orientation())
    sleep(0.1)
