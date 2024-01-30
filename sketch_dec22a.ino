#include <Servo.h>
char serialRead;
Servo servo;
int speed = 150;
int relay = 6;

void setup() {
Serial.begin(115200);
pinMode(2, OUTPUT); //enB
pinMode(3, OUTPUT); // motor A 
pinMode(4, OUTPUT); // motor B 
pinMode(5, OUTPUT); //enA
pinMode(relay, OUTPUT); // relay untuk pompa
servo.attach(8);
servo.write(0);
}

void loop() {
 if (Serial.available() > 0) {
    serialRead = Serial.read();

    switch (serialRead) {
      case 'A':
        digitalWrite(relay, LOW);
        servo.write(0);
        matiMotorA();
        matiMotorB();
        break;
      case 'B':
        digitalWrite(relay, HIGH);
        servo.write(0);
        matiMotorA();
        matiMotorB();
        break;

      case 'C': 
        servo.write(0);
        nyalaMotorA();
        nyalaMotorB();
        break;
      case 'D':
        servo.write(90);
        matiMotorA();
        matiMotorB();
        break;
      case 'E':
        servo.write(180);
        matiMotorA();
        matiMotorB();
        break;
      case 'F':
        servo.write(90);
        nyalaMotorA();
        nyalaMotorB();     
        break ;

      case 'G':
        servo.write(0);
        nyalaMotorA();
        matiMotorB();
        break;

      case 'H': 
        servo.write(0);
        matiMotorA();

        break;
      case 'J':
        servo.write(90);
        nyalaMotorA();
        nyalaMotorB();
        break;
    }
 }
}

void nyalaMotorA() {
  analogWrite(5, speed);
  digitalWrite(3, HIGH);
}

void matiMotorA() {
 digitalWrite(3, LOW);
}

void nyalaMotorB() {
 analogWrite(2, speed);
 digitalWrite(4, HIGH);
}

void matiMotorB() {
 digitalWrite(4, LOW);
}