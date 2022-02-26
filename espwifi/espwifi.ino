#include <SoftwareSerial.h>
#include <DHT.h>
#define RX 2
#define TX 3
#define DHTPIN 4
#define DHTTYPE DHT1
int analogPinsm = A0;
int analogPinldr = A2;
DHT dht(DHTPIN, DHTTYPE);
String AP = "Wifi NAME";       // AP NAME
String PASS = "Wifi Password"; // AP PASSWORD
String API = "K8ZLCA9UWXGD9RX5";   // Write API KEY
String HOST = "api.thingspeak.com";
String PORT = "80";
String field = "field1";
String field2 = "field2";
String field3 = "field3";
String field4 = "field4";
int countTrueCommand;
int countTimeCommand; 
boolean found = false; 
SoftwareSerial esp8266(RX,TX); 

int moisture;
int percentage;
int soilm;
int ldrvalue;
int ldrv;
float tempt;
float humid;
int map_low = 650;
int map_high = 350;

void setup() {
  Serial.begin(9600);
  dht.begin();
  esp8266.begin(115200);
  sendCommand("AT",5,"OK");
  sendCommand("AT+CWMODE=1",5,"OK");
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK");
}

void loop() {
  
  soilm = soilmdata();
  //Serial.print(" SOIL MOISTURE Percentage: ");
  Serial.println(soilm);
  //Serial.println("%");
  ldrv = ldrdata();
  //Serial.println(" LDR Value: ");
  Serial.println(ldrv);
  //Serial.println(" ");
  tempt = temp();
  //Serial.print(" TEMP: ");
  Serial.println(tempt);
  humid = hum();
  //Serial.print(" HUM: ");
  Serial.println(humid);
  Serial.println(" ");
  String getData = "GET /update?api_key="+ API +"&"+ field +"="+String(soilm)+"&"+ field2 +"="+String(ldrv)+ field3 +"="+String(tempt)+ field4 +"="+String(humid);
  sendCommand("AT+CIPMUX=1",5,"OK");
  sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
  sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
  esp8266.println(getData);delay(1500);countTrueCommand++;
  sendCommand("AT+CIPCLOSE=0",5,"OK");
  delay(1000);
}


int  soilmdata(){
  moisture = analogRead(analogPinsm);
  percentage = map(moisture, map_low, map_high, 0, 100);
  return percentage;
}
int ldrdata(){
  ldrvalue = analogRead(analogPinldr);
  return ldrvalue;
}
float temp(){
  float t = dht.readTemperature();
  return t;
}
float hum(){
  float h = dht.readHumidity();
  return h;
}

void sendCommand(String command, int maxTime, char readReplay[]) {
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);//at+cipsend
    if(esp8266.find(readReplay))//ok
    {
      found = true;
      break;
    }
  
    countTimeCommand++;
  }
  
  if(found == true)
  {
    Serial.println("OYI");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fail");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
 }

 
