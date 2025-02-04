#include <WiFi101.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <WiFiSSLClient.h>
#include <WiFiUdp.h>
#include <SPI.h>
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIXEL_PIN      7    // Data Pin of Led strip 
#define PIXEL_COUNT    57   // Number of LEDs in the strip
#define BRIGHTNESS   250   // use 96 for medium brightness
#define SPEED         0  // Speed of each Color Transition (in ms)
#define IMMEDIATELY    0    // Transition happen instantly
#define RAINBOW_SPEED  50    // Rainbow Transition speed
Adafruit_NeoPixel strip = Adafruit_NeoPixel(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
bool offOld = LOW;
bool WhiteOld = LOW;
bool RedOld = LOW;
bool GreenOld = LOW;
bool BlueOld = LOW;
bool TopazOld = LOW;
bool LilacOld = LOW;
bool RainbowOld = LOW;
bool rgbOld = LOW;
int  showType = 0;
boolean reading = false;
String myStr;
int redVal, greenVal, blueVal;

char ssid[] = "TerryOP6"; //  your network SSID (name)
char pass[] = "19950727"; // your network password
int keyIndex = 0;                 // your network key Index number (needed only for WEP)
int ledpin = 6;
bool val = true;
 
int status = WL_IDLE_STATUS;
WiFiServer server(80);
 
void setup() {
  Serial.begin(9600);      // initialize serial communication
  Serial.print("Start Serial ");
  strip.setBrightness(BRIGHTNESS);  
  strip.begin();
  strip.show();
  pinMode(ledpin, OUTPUT);      // set the LED pin mode
  // Check for the presence of the shield
  Serial.print("WiFi101 shield: ");
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("NOT PRESENT");
    return; // don't continue
  }
  Serial.println("DETECTED");
  // attempt to connect to Wifi network:
  while ( status != WL_CONNECTED) {
    digitalWrite(ledpin, LOW);
    Serial.print("Attempting to connect to Network named: ");
    Serial.println(ssid);                   // print the network name (SSID);
    digitalWrite(ledpin, HIGH);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);
    // wait 10 seconds for connection:
    delay(10000);
  }
  server.begin();                           // start the web server on port 80
  printWifiStatus();                        // you're connected now, so print out the status
  digitalWrite(ledpin, HIGH);
}

void setcolour(int r, int g, int b)
{
  colorWipe(strip.Color(r, g, b), SPEED);
}

void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void loop() {
  WiFiClient client = server.available();   // listen for incoming clients
  if (client) {                             // if you get a client,
    Serial.println("new client");           // print a message out the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    while (client.connected()) {            // loop while the client's connected
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c);                    // print it out the serial monitor
        if (c == '\n') {                    // if the byte is a newline character
          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();
            // the content of the HTTP response follows the header:
            client.print("<a href=\"/W\">on</a>    <br>");
            client.print("<a href=\"/D\">off</a>    <br>");
            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:
            //form added to send data from browser and view received data in serial monitor         
            break;
          }
          else {      // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        }
        else if (c != '\r') {    // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
        getRGB(currentLine);
        // Check to see if the client request was "GET /H" or "GET /L":
        if (currentLine.endsWith("GET /W")) {
          setcolour(255,255,255);
          getRGB(currentLine);
        }
        if (currentLine.endsWith("GET /D")) {
          setcolour(0,0,0);

        }
      }
    }
    // close the connection:
    client.stop();
    Serial.println("client disonnected");
  }
}
// find the RGB in post lines
 void getRGB(String Lines){
  int r,g,b;
  int x = Lines.indexOf("_light");
  if (x != -1){
      if(Lines.endsWith("_light")){
        //Serial.print("`````get the end of RGB!!!``````` ");
        Serial.print(Lines);
        r = Lines.substring(6,9).toInt();
        g = Lines.substring(10,13).toInt();
        b = Lines.substring(14,17).toInt();
        setcolour(r,g,b);
      }
  }
} 
void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
 
  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
 
  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
  // print where to go in a browser:
  Serial.print("To see this page in action, open a browser to http://");
  Serial.println(ip);
}
