#include <Wire.h>

#define SLAVE_ADDR 8 // Address of the Pico on the I2C bus

void setup() {
  Wire.begin(SLAVE_ADDR);     // Initialize as I2C slave with address 8
  Wire.onRequest(requestEvent);  // Define what to do when the master requests data
  Wire.onReceive(receiveEvent);  // Define what to do when data is received
}

void loop() {
  delay(100);  // Main loop does nothing, waiting for I2C events
}

// Function to send data back to the master when requested
void requestEvent() {
  Wire.write("Hello from Pico");  // Respond with a message
}

// Function to receive data from the master
void receiveEvent(int byteCount) {
  while (Wire.available()) {
    char c = Wire.read();  // Read each byte
    Serial.print(c);       // Print the received data to Serial Monitor
  }
}
