import serial
import json
import random

arduino = serial.Serial("/dev/ttyACM0", 9600)
arduino.flushInput()

while True:
    if arduino.inWaiting() > 0:
        linea = arduino.readline().decode("UTF-8")
        try:
            datos = json.loads(linea)
            print("luz = " + str(datos["luz"]))
            enc = "off"
            if random.randrange(2) == 1:
                enc = "on"
            pkt = json.dumps({"led": enc});
            arduino.write((pkt + "\n").encode("UTF-8"))
        except ValueException:
            pass
        except Exception as e:
            print(e)

