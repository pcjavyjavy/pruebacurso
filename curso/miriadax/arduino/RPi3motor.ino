const int Izquierda = 2; // L293D H-bridge-7
const int Derecha = 3; // L293D H-bridge-2
const int Encender = 9;   // L293D H-bridge-1
const int EntradaIzquierda = A0;  // velocidades que manda la RPi3
const int EntradaDerecha = A1;

int VelocidadIzquierda = 0; // velocidades del motor
int VelocidadDerecha = 0;


void setup() {
  pinMode(Izquierda, OUTPUT);
  pinMode(Derecha, OUTPUT);
  pinMode(Encender, OUTPUT);
  //Empezamos con el motor apagado
  digitalWrite(Encender, LOW);
}

void loop() {

  delay(1);
  
  VelocidadIzquierda = analogRead(EntradaIzquierda) / 4;
  VelocidadDerecha = analogRead(EntradaDerecha) / 4;
  // Vamos hacia donde mayor sea la velocidad
  if (VelocidadIzquierda >= VelocidadDerecha) {
    digitalWrite(Izquierda, HIGH);
    digitalWrite(Derecha, LOW);
    analogWrite(Encender, VelocidadIzquierda);
  } else {
    digitalWrite(Izquierda, LOW);
    digitalWrite(Derecha, HIGH);
    analogWrite(Encender, VelocidadDerecha);
  }

}
