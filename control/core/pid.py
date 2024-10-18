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


