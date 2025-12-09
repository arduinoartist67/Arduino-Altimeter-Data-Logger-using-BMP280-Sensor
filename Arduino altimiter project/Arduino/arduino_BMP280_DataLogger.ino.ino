#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <Adafruit_BMP280.h>

const int chipSelect = 10;
Adafruit_BMP280 bmp;
unsigned long startTime = 0;

void setup() {
  Serial.begin(9600);

  if (!bmp.begin(0x76)) {
    Serial.println("Error: BMP280 not found");
    while (1);
  }

  if (!SD.begin(chipSelect)) {
    Serial.println("Error: SD card init failed");
    while (1);
  }

  File file = SD.open("data.csv", FILE_WRITE);
  if (file) {
    file.println("time,altitude,pressure,temperature");
    file.close();
  }

  startTime = millis();
}

void loop() {
  float timeSec = (millis() - startTime) / 1000.0;
  float pressure = bmp.readPressure() / 100.0;
  float temperature = bmp.readTemperature();
  float altitude = bmp.readAltitude(1013.25);

  File dataFile = SD.open("data.csv", FILE_WRITE);
  if (dataFile) {
    dataFile.print(timeSec, 2);
    dataFile.print(",");
    dataFile.print(altitude, 2);
    dataFile.print(",");
    dataFile.print(pressure, 2);
    dataFile.print(",");
    dataFile.println(temperature, 2);
    dataFile.close();
  }

  delay(1000);
}
