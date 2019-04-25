int val = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly
  float temp;
  val = analogRead(A0);
  temp = (((val*3.3)/1023)+18.558)/(0.9429);
  Serial.printf("%.2f %d %.2f\n", temp, val, (val*3.3)/1023);
  delay(510);
}
