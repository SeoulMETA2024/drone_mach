from motor import Motor
from pid import PID, PIDValueing
from sensor import Sensor, KalmanFilter


#조립 후 기재하기
BUS_NUM = 1
SERIAL_NUM = 1
class Hover(KalmanFilter):
    def __init__(self,motor_1,motor_2,motor_3,motor_4,Kp,Ki,Kd) -> None:
        self.PIDValueing = PIDValueing()

        self.sensor = Sensor(BUS_NUM, SERIAL_NUM)

        self.motor_1 = Motor(motor_1)
        self.motor_2 = Motor(motor_2)
        self.motor_3 = Motor(motor_3)
        self.motor_4 = Motor(motor_4)

        self.KalmanFilter_x = KalmanFilter()
        self.KalmanFilter_y = KalmanFilter()
        self.KalmanFilter_z = KalmanFilter()

        self.angle = 0

        super().__init__(Kp,Ki,Kd)
        
        sensor = Sensor()
        pass




    def alleviate(self,target_pitch,target_roll,target_thrust) -> None:

        

        data = self.sensor.measure()

        pitch = data[0]
        roll = data[1]        


        motor_1_duty, motor_2_duty, motor_3_duty, motor_4_duty = self.PIDValueing.update_duty(target_pitch,target_roll,target_thrust, gyro_x, gyro_y, gyro_z)

        

        self.motor_1.motor_cycle(motor_1_duty)
        self.motor_2.motor_cycle(motor_2_duty)
        self.motor_3.motor_cycle(motor_3_duty)
        self.motor_4.motor_cycle(motor_4_duty)

        return 


            



            



            