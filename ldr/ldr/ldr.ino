#include <ArduinoJson.h>
#define LDR A0

void setup() {
  Serial.begin(9600);
  pinMode(LDR, INPUT);
}

void loop() {
  StaticJsonDocument<1024> doc;
  int luz = analogRead(LDR);
  doc["luz"] = luz;
  serializeJson(doc, Serial);
  Serial.println();
  delay(1000);
}
