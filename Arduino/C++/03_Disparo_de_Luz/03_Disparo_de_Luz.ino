const int ledPin1 = 1;
const int ledPin2 = 2;
const int ledPin3 = 3;
int EstadoBoton = 0;

void setup() {
  pinMode(EstadoBoton, INPUT);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}

void loop() {
  EstadoBoton = digitalRead(4);
  if (EstadoBoton == LOW) {
    digitalWrite(ledPin1, HIGH);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, LOW);
  }
  else  {
    digitalWrite(ledPin1, LOW);
    digitalWrite(ledPin2, LOW);
    digitalWrite(ledPin3, HIGH);

    delay(250);
    digitalWrite(ledPin2, HIGH);
    digitalWrite(ledPin3, LOW);
    delay(250);
  }
}
