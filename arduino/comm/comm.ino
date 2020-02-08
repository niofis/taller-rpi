#include <ArduinoJson.h>

String linea = "";
bool lineaDisponible = false;

void setup() {
  // Inicializa puerto serial
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  // Crea un objeto json, agrega un dato y lo envia
  StaticJsonDocument<1024> doc;
  doc["luz"] = 512;
  serializeJson(doc, Serial);
  Serial.println();

  if (lineaDisponible) {
    lineaDisponible = false;
    
    DeserializationError error = deserializeJson(doc, linea);
    if (!error) {
      if (doc["led"] == "off") {
        digitalWrite(LED_BUILTIN, LOW);
      } else if (doc["led"] == "on") {
        digitalWrite(LED_BUILTIN, HIGH);
      }
    } else {
      Serial.print(F("deserializeJson() failed: "));
      Serial.println(error.c_str());
    }
  }
  
  delay(1000);
}

void serialEvent() {
  linea = "";
  while (Serial.available()) {
    char chr = (char)Serial.read();
    linea += chr;
    if (chr == '\n') {
      lineaDisponible = true;
    }
  }
}
