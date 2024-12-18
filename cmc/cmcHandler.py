import math

def cmcHandler(msg):

    #msg: array(front/back, right/left, top/down) - -255~255 값으로 정규화된 값을 가진 tuple
    #target velocity을 target angle로 변화하는 과정 구현하기
    #angle 기반 pid

    fb_v = msg[0]
    rl_v = msg[1]
    h_v = msg[2]

    pitch = math.acos(fb_v/255)
    roll = math.acos(fb_v/255)
    thrust = h_v / 255
    
    return (pitch, roll, thrust)
    
    

