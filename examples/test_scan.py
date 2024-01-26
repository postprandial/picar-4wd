# test: hold obstacle in front of car at distance cm
# car should turn right but stay in position
# the put another obstacle in front of car
# use to test angle, etc.
# to be deleted later
import time

import picar_4wd as fc

speed = 5 # slow
distance = 25 # 25 centimeter, argument for scan_step below

def main():
    test_round = 1
    while True:
        print(f"round {test_round} begins")
        scan_list = fc.scan_step(distance) # scan_step returns a list containing 10 samples from the ultrasonic module
        # taken every 18 degrees (for a 180 degree field). It looks for obstacles at a distance of up to
        # 25 centimers (the value of distance).
        if not scan_list:
            continue

        tmp = scan_list[3:7] # out of 10 samples, this list slice keeps samples 4,5,6,7, so the area in front of
        # the car (it discards samples taken from the sides, ie. more than 36 degree to either left or right).
        print(f"This is tmp: {tmp}")
        print(f"This is scan_list: {scan_list}")
        if tmp != [2,2,2,2]: # 2 seems to mean "no obstacle". If those samples from the front
            # (0 - 36 degrees left/right) are not 2, that means an obstacle exists here.
            fc.turn_right(speed)
            time.sleep(1)
            fc.stop()
        else:
            pass
        print(f"Next round in 3 seconds")
        time.sleep(3) # this buys us 3 seconds before the next round to reset the obstacle
        test_round += 1


if __name__ == "__main__":
    try:
        print("Start")
        main()
    finally:
        fc.stop()
