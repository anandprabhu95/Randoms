#include <Arduino.h>

int ledPin = 13; // Built-in LED pin
int pirPin = 12; // HC-S501 data pin
int buzzPin = 3; // Buzzer pin
int pirValue;    // Value of PIR
int toneFreq = 4186
int buzzTime = 1000 // BuzzTime ms

void setup() {
  Serial.begin(57600);
  pinMode(ledPin, OUTPUT);   // Set LED pin as output
  pinMode(pirPin, INPUT);    // Set pirPin as input
  pinMode(buzzPin, OUTPUT);
  digitalWrite(ledPin,LOW);  // Turn off builtin LED
}

void loop() {
  pirValue = digitalRead(pirPin); // Read PIR value
  Serial.println(pirValue);
  digitalWrite(ledPin, pirValue);
  if (pirValue == 1) 
  {
    tone(buzzPin, toneFreq, buzzTime);
  }
}
 