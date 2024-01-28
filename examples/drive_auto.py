
import time
import random

import picar_4wd as fc

speed = 5 # slow
turn_speed = 20
distance = 35 # 25 centimeter, argument for scan_step below

def random_direction():
    '''picks either left or right and time period between 0.5 and 2 seconds for turning '''
    turns = [fc.turn_left, fc.turn_right]
    turn_duration = random.uniform(1, 2)
    turn_direction = turns[random.randint(0,1)]
    return turn_direction, turn_duration


# directions = [fc.forward, fc.backward] not sure yet if I need this


def main():
    test_round = 1
    #last_direction = fc.forward
    while True:
        print(f"round {test_round} begins")
        fc.forward(speed)
        scan_list = fc.scan_step(distance) # scan_step returns a list containing 10 samples from the ultrasonic module
        # taken every 9 degrees (for a 90 degree field). It looks for obstacles at a distance of up to
        # 35 centimeters (the value of distance).
        if not scan_list:
            continue

        tmp = scan_list[2:8] # out of 10 samples, this list slice keeps samples 3,4,5,6,7,8 so the area in front of
        # the car (it discards samples taken from the sides)
        print(f"This is tmp: {tmp}")
        print(f"This is scan_list: {scan_list}")
        if tmp != [2,2,2,2,2,2]: # 2 seems to mean "no obstacle". If those samples from the front
            # for now, simply backs up only for one second
            fc.backward(speed)
            time.sleep(1)
            fc.stop()
            # picks random new direction
            turn_this_way, duration = random_direction()
            turn_this_way(turn_speed) #this is faster for obvious reasons
            time.sleep(duration)
            fc.stop()
        test_round += 1


if __name__ == "__main__":
    try:
        print("Start")
        main()
    finally:
        fc.stop()
