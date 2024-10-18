from motor import Motor
from pid import PID
from sensor import Sensor

class Hover(PID):
    def __init__(self,motor_1,motor_2,motor_3,motor_4,Kp,Ki,Kd):

        self.motor_1 = Motor(motor_1)
        self.motor_2 = Motor(motor_2)
        self.motor_3 = Motor(motor_3)
        self.motor_4 = Motor(motor_4)

        self.angle = 0

        super().__init__(Kp,Ki,Kd)
        
        sensor = Sensor()
        pass

    def hover_hor(self):

        target_angle = 0
        current_angle = 5 #받아오기
        while True:
            self.pid_compute(target_angle,current_angle)