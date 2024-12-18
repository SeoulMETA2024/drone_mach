from control.core.hovering import Hover
from cmc.cmc_machine import cmc_main, cmc_run

Drone = Hover()

if __name__ == "main":
    
    is_Running = False

    while is_Running:
        command = input("Type 'run' to start. ")
        if command == 'run':
            is_Running = True
        else:
            pass

    while is_Running:

        x = 
        y = 
        z = 
        thrust =

        
        
        

        Drone.alleviate(x,y,z,thrust)

        
        

    
        
    