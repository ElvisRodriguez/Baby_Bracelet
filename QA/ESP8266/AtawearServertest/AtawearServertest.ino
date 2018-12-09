#include <ESP8266WebServer.h>
#include <ESP8266WebServerSecure.h>
#include <ESP8266WebServerSecureAxTLS.h>
#include <ESP8266WebServerSecureBearSSL.h>

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <WiFiManager.h>
#include <DNSServer.h>
#define heartratePin A0
uint8_t rateValue;
#include <DFRobot_Heartrate.h>
const char index_html[] PROGMEM={"<!DOCTYPE html>\n<html>\n<title>Atawear</title>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<body style=\"background:#33ccff\">\n\t<h1 style=\"color:black\", align=\"center\">Atawear</h1>\n    <hr style=\"margin:auto;width:100%\">\n    <p align=\"center\"><a href=\"https://elvisrodriguez.pythonanywhere.com/\">Click here</a></p>\n  </div>\n  </body>\n</html>"};
ESP8266WebServer server(80);
DFRobot_Heartrate heartrate(DIGITAL_MODE); ///< ANALOG_MODE or DIGITAL_MODE

void handleRoot() {
  
  server.send_P(200, "text/html", index_html);
}

void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";

  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }

  server.send(404, "text/plain", message);
}
//Use this if you need to do something when your device enters configuration mode on failed WiFi connection attempt.
void configModeCallback (WiFiManager *myWiFiManager) {
  Serial.println("Entered config mode");
  Serial.println(WiFi.softAPIP());

  Serial.println(myWiFiManager->getConfigPortalSSID());
}

void setup(void) {
  Serial.begin(115200);
  Serial.println("Starting");
  WiFiManager wifiManager;
  wifiManager.resetSettings();
  wifiManager.setAPCallback(configModeCallback);
  wifiManager.autoConnect("Atawear","Atawear01");
  //wifiManager.setConfigPortalTimeout(60);
  WiFi.mode(WIFI_STA);

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 // Prompts information about connected network's IP
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(WiFi.status());
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);
  server.on("/inline", []() {
    server.send(200, "text/plain", "this works as well");
  });
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
  heartrate.getValue(heartratePin); ///< A0 foot sampled values
  rateValue = heartrate.getRate(); ///< Get heart rate value
  if (rateValue){
    Serial.println(rateValue);
  }
  delay(1000);
}
