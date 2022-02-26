#include <DHT.h>
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

int analogPinsm = A0;
int analogPinldr = A2;
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
  //pinMode(ldrPin, INPUT);
  dht.begin();
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


 
