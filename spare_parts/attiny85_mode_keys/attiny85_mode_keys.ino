#include "DigiKeyboard.h"

// this constant won't change:
const int  mode_button = 0;    // the pin that the pushbutton is attached to
const int  button = 2;    // the pin that the pushbutton is attached to
const int ledPin = 1;       // the pin that the LED is attached to

// Variables will change:
int mode_buttonPushCounter = 0;   // counter for the number of button presses
int mode_buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button

//jack
int jackState = 0; 

void setup() {
  // initialize the button pin as a input:
  pinMode(mode_button, INPUT_PULLUP);
  pinMode(button, INPUT_PULLUP);
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // this is generally not necessary but with some older systems it seems to
  // prevent missing the first character after a delay:
  DigiKeyboard.sendKeyStroke(0);
  
  // read the pushbutton input pin:
  mode_buttonState = digitalRead(mode_button);

  // compare the buttonState to its previous state
  if (mode_buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (mode_buttonState == LOW) {
      // if the current state is HIGH then the button went from off to on:
      mode_buttonPushCounter++;
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state, for next time through the loop
  lastButtonState = mode_buttonState;

  if (mode_buttonPushCounter == 2){
    mode_buttonPushCounter = 0;
  }

  // read the pushbutton input pin:
  jackState = digitalRead(button); //3.5mm jack
  delay(100);

  if (mode_buttonPushCounter == 0 && jackState == false) {
    digitalWrite(ledPin, HIGH);
    DigiKeyboard.sendKeyStroke(KEY_SPACE); // press and release SPACE
    delay(100);
  } else {
    digitalWrite(ledPin, LOW);
  }

  if (mode_buttonPushCounter == 1 && jackState == false) {
    digitalWrite(ledPin, HIGH);
    DigiKeyboard.sendKeyStroke(KEY_ENTER); // press and release SPACE
    delay(100);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
