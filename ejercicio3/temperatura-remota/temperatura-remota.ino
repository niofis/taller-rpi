#include <ESP8266WiFi.h>
#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include <DHT.h>

#define WLAN_SSID       "NSA"
#define WLAN_PASS       "****"

#define MQTT_SERVER      "192.168.50.105"
#define MQTT_SERVERPORT  1883

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

WiFiClient client;

Adafruit_MQTT_Client mqtt(&client, MQTT_SERVER, MQTT_SERVERPORT);

Adafruit_MQTT_Publish temperatura = Adafruit_MQTT_Publish(&mqtt, "sensor/temperatura");
Adafruit_MQTT_Publish humedad = Adafruit_MQTT_Publish(&mqtt, "sensor/humedad");

void MQTT_connect();

void setup() {
  Serial.begin(115200);
  delay(10);

  Serial.println("Sensor de temperatura remoto");

  Serial.println(); Serial.println();
  Serial.print("Conectando a ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.println("IP address: "); Serial.println(WiFi.localIP());
  
  dht.begin();
}

void loop() {
  MQTT_connect();

  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  if (isnan(t)) {
    t = -999;
  }
  if (isnan(h)) {
    h = -999;
  }
  
  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print(" Humedad: ");
  Serial.println(h);
  
  if (!temperatura.publish(t)) {
    Serial.println(F("Fallo enviando temperatura"));
  }

  if (!humedad.publish(h)) {
    Serial.println(F("Fallo enviando humedad"));
  }

  delay(5000);
}

// Function to connect and reconnect as necessary to the MQTT server.
// Should be called in the loop function and it will take care if connecting.
void MQTT_connect() {
  int8_t ret;

  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }

  Serial.print("Connecting to MQTT... ");

  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
       Serial.println(mqtt.connectErrorString(ret));
       Serial.println("Retrying MQTT connection in 5 seconds...");
       mqtt.disconnect();
       delay(5000);  // wait 5 seconds
       retries--;
       if (retries == 0) {
         // basically die and wait for WDT to reset me
         while (1);
       }
  }
  Serial.println("MQTT Connected!");
}
