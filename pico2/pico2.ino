#include <Wire.h>

#define I2C_ADDRESS 0x08  // Must match what Pi is looking for

void setup() {
  Wire.begin(I2C_ADDRESS);            // Start as slave
  Wire.onReceive(receiveEvent);       // What to do when master writes
  Wire.onRequest(requestEvent);       // What to do when master reads
  Serial.begin(115200);
  Serial.println("Pico I2C Slave Ready");
}

void loop() {
  delay(100);
}

void receiveEvent(int len) {
  Serial.print("Recv: ");
  while (Wire.available()) {
    char c = Wire.read();
    Serial.print(c);
  }
  Serial.println();
}

void requestEvent() {
  Wire.write("Hi Pi");
}
