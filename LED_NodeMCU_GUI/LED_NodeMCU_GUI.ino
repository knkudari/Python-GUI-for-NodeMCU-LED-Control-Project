#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "your_wifi_ssid";
const char* password = "your_wifi_password";

ESP8266WebServer server(80);

int led1Pin = D0;
int led2Pin = D1;
int led3Pin = D2;
int led4Pin = D3;

void setup() {
  Serial.begin(115200);

  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  pinMode(led3Pin, OUTPUT);
  pinMode(led4Pin, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("NodeMCU IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/led1", HTTP_GET, []() {
    digitalWrite(led1Pin, !digitalRead(led1Pin));
    server.send(200, "text/plain", "LED 1 toggled");
  });

  server.on("/led2", HTTP_GET, []() {
    digitalWrite(led2Pin, !digitalRead(led2Pin));
    server.send(200, "text/plain", "LED 2 toggled");
  });

  server.on("/led3", HTTP_GET, []() {
    digitalWrite(led3Pin, !digitalRead(led3Pin));
    server.send(200, "text/plain", "LED 3 toggled");
  });

  server.on("/led4", HTTP_GET, []() {
    digitalWrite(led4Pin, !digitalRead(led4Pin));
    server.send(200, "text/plain", "LED 4 toggled");
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
