#include <ESP8266WiFi.h>
const char* ssid = "Jo";
const char* password = "0813065241";

const char* host = "maker.ifttt.com";
const char* privateKey = "cHN_9LjAj1e3lvoZS09OLg";
const char* event = "Alert";
int count1 = 0, count2 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10);
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED){
      delay(500);
      Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  // Print the IP address
  Serial.print("IP=");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
  int val = analogRead(A0);
  if (val < 500 && count2 == 0)
      count2 = 1;
  Serial.println(val);
  if (val > 500 && count2 == 1){
    count2 = 0;
    line(++count1);
  }
}
