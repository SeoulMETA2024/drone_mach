from control.core.hovering import Hover
from cmc.cmc_machine import RemoteControl

Drone = Hover()

if __name__ == "main":
    
    is_Running = False

    Server = RemoteControl()

    while is_Running:
        command = input("Type 'run' to start. ")
        if command == 'run':
            is_Running = True
        else:
            pass

    while is_Running:

        pitch, roll, thrust = Server.res            

        Drone.alleviate(pitch,roll,thrust)

        
        

    
        
    