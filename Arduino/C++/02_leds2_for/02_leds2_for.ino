 // 01_leds2_for

const int ledPin1 = 9;
const int ledPin2 = 10;
const int tiempo = 1000;

void setup() {
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() {
  for (int tiempo = 1 ; tiempo < 1000 ; tiempo = tiempo + 10) {
    digitalWrite(ledPin1, HIGH);
    digitalWrite(ledPin2, LOW);
    delay(tiempo);
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, HIGH);
    delay(tiempo);
 } 
}
