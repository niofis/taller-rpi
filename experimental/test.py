from time import sleep
from remote import initConnection, get_geolocation, get_orientation 

initConnection(url='https://127.0.0.1:3443', id=1234)
while True:
    print(get_orientation())
    print(get_geolocation())
    sleep(0.1)
