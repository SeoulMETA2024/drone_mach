  #include Servo.h

int Spd_1 = 30;
int Spd_2 = 30;
int Spd_3 = 30;
int Spd_4 = 30;

Servo motor_1;
Servo motor_2;
Servo motor_3;
Servo motor_4;

int pin_1 = 1;
int pin_2 = 2;
int pin_3 = 3;
int pin_4 = 4;

void setup() {
  Serial.begin(9600);

  motor_1.attatch(1);
  motor_2.attatch(2);
  motor_3.attatch(3);
  motor_4.attatch(4);

  motor_1.write(Spd_1);
  motor_2.write(Spd_2);
  motor_3.write(Spd_3);
motor_4.write(Spd_4);

  delay(3000);

  // put your setup code here, to run once:

}

void loop() {
  if Serial.available() {
    int input = Serial.read();
    
    switch(input){

      case 1:
        Spd_1 += 1;

      case 2:
        Spd_1 -= 1;

      case 3:
        Spd_2 += 1;

      case 4:
        Spd_2 -= 1;

      case 5:
        Spd_3 += 1;

      case 6:
        Spd_3 -= 1;
      case 7:
        Spd_4 += 1;

      case 8: 
        Spd_4 -= 1;

      case 9:
        break;
    }

  }
  // put your main code here, to run repeatedly:

}
