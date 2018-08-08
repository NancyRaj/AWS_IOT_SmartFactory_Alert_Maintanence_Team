//Code is for reading the data from LM35 and sending it via serial communication
int spin=A2;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int bitval=analogRead(spin);
float volt=float(bitval)*5/1023;
int temp=volt*100;
Serial.println(temp);
delay(2000);
}

