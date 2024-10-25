const int botonPin = 2;
const int sensorPin = A0;
const int ledPin = 13;
const int umbralHumedad = 500;

unsigned long tiempoAnteriorRiego = 0;
const unsigned long intervaloRiego = 5000; // 5 segundos en milisegundos
const unsigned long duracionRiego = 2000; // 2 segundos en milisegundos

void setup() {
  pinMode(botonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int valorSensor = analogRead(sensorPin);
  Serial.print("Humedad: ");
  Serial.println(valorSensor);

  unsigned long tiempoActual = millis();

  if (digitalRead(botonPin) == LOW || valorSensor < umbralHumedad) {
    // Encendido manual o por sensor
    digitalWrite(ledPin, HIGH);
    delay(duracionRiego);
    digitalWrite(ledPin, LOW);
  } else {
    // Riego automático
    if (tiempoActual - tiempoAnteriorRiego >= intervaloRiego) {
      digitalWrite(ledPin, HIGH);
      delay(duracionRiego);
      digitalWrite(ledPin, LOW);
      tiempoAnteriorRiego = tiempoActual;
    }
  }
}