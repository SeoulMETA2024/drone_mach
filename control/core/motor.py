import RPi.GPIO as GPIO

class Motor:
    def __init__(self, pin):

        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

        
        self.pwm = GPIO.PWM(self.pin, 1000)

        self.pwm.start(0)

        pass
    
    '''change duty cycle of the motor'''
    def motor_cycle(self,cycle):

        self.pwm.ChangeDutyCycle(cycle)
        print(cycle)

        return
        