import sys
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
        except KeyboardInterrupt:
            sys.exit()
        except ValueError:
            pass
        except Exception as e:
            print(e)

