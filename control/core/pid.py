class PID:
    def __init__(self, kP, kI, kD):

        self.kP = kP
        self.kI = kI
        self.kD = kD   

        self.integral = 0
        self.prev_err = 0
        pass
    
    '''Compute Pid Value'''
    def compute(self, setpoint, current_value):
        err = setpoint - current_value

        self.integral += err

        derivative = err - self.prev_err
        self.prev_err = err

        value = err*self.kP + self.integral*self.kI + derivative*self.kD


        return value

    

class PIDValueing(PID):
    '''Apply PID in Drone'''

    def __init__(self,aP,aI,aD,hP,hI,hD,heightWeight):
         self.anglePID = PID(aP,aI,aD)

         self.heightPID = PID(hP,hI,hD)

         self.weight = heightWeight

         pass
    
    
    def update_duty(self, target_x:float, target_y:float, target_z:float, thrust,current_x:float,current_y:float,current_z:float) -> float: 
            '''Update Duty Cycle based on Computed PID Value'''
            pid_x = self.anglePID(target_x,current_x)
            pid_y = self.anglePID(target_y,current_y)
            pid_z = self.anglePID(target_z,current_z)


            motor_1_duty = self.weight*thrust + pid_x + pid_y - pid_z
            motor_2_duty = self.weight*thrust - pid_x + pid_y + pid_z
            motor_3_duty = self.weight*thrust - pid_x - pid_y - pid_z
            motor_4_duty = self.weight*thrust + pid_x - pid_y + pid_z

       
            motor_1_duty = max(0, min(100, motor_1_duty))
            motor_2_duty = max(0, min(100, motor_2_duty))
            motor_3_duty = max(0, min(100, motor_3_duty))
            motor_4_duty = max(0, min(100, motor_4_duty))

            return motor_1_duty, motor_2_duty, motor_2_duty, motor_4_duty


