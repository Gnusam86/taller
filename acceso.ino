const int buttonPin = 2;
const int servoPin = 9;
const int ledPin = 13;

int contraseña[] = {1, 1, 0, 1}; // Contraseña: dos pulsaciones, espera, una pulsación
int pulsaciones[10]; // Arreglo para almacenar las pulsaciones del usuario
int indicePulsacion = 0; 
unsigned long tiempoInicio = 0;
const unsigned long tiempoLimite = 5000; // Tiempo límite para ingresar la contraseña (5 segundos)

Servo miServo;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
  miServo.attach(servoPin);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH && tiempoInicio == 0) {
    tiempoInicio = millis(); // Inicia el conteo del tiempo
  }

  if (buttonState == HIGH && millis() - tiempoInicio < tiempoLimite) {
    pulsaciones[indicePulsacion] = 1;
    indicePulsacion++;
    delay(500); // Evita lecturas múltiples del botón
  } else if (buttonState == LOW && millis() - tiempoInicio < tiempoLimite) {
    pulsaciones[indicePulsacion] = 0;
    indicePulsacion++;
    delay(500);
  }

  if (millis() - tiempoInicio >= tiempoLimite) {
    if (compararSecuencias(pulsaciones, contraseña, indicePulsacion)) {
      Serial.println("Acceso permitido");
      digitalWrite(ledPin, HIGH);
      miServo.write(90);
      delay(3000);
      miServo.write(0);
      digitalWrite(ledPin, LOW);
    } else {
      Serial.println("Acceso denegado");
    }
    // Reinicia las variables para la siguiente entrada
    indicePulsacion = 0;
    tiempoInicio = 0;
  }
}

boolean compararSecuencias(int pulsaciones[], int contraseña[], int longitud) {
  // Compara las secuencias de pulsaciones
  for (int i = 0; i < longitud; i++) {
    if (pulsaciones[i] != contraseña[i]) {
      return false;
    }
  }
  return true;
}