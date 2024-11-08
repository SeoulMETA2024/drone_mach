class PID:
    def __init__(self, kP, kI, kD):

        self.kP = kP
        self.kI = kI
        self.kD = kD   

        self.integral = 0
        self.prev_err = 0
        pass
    
    def pid_compute(self, setpoint, current_value):
        err = setpoint - current_value

        self.integral += err

        derivative = err - self.prev_err
        self.prev_err = err

        value = err*self.kP + self.integral*self.kI + derivative*self.kD


        return value

    def update_duty(self, pid_x, pid_y, pid_z):
            motor_1_duty = 50 + pid_x + pid_y - pid_z
            motor_2_duty = 50 - pid_x + pid_y + pid_z
            motor_3_duty = 50 - pid_x - pid_y - pid_z
            motor_4_duty = 50 + pid_x - pid_y + pid_z

       
            motor_1_duty = max(0, min(100, motor_1_duty))
            motor_2_duty = max(0, min(100, motor_2_duty))
            motor_3_duty = max(0, min(100, motor_3_duty))
            motor_4_duty = max(0, min(100, motor_4_duty))

            return motor_1_duty, motor_2_duty, motor_2_duty, motor_4_duty
    
    

