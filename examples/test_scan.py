# test: hold obstacle in front of car at distance cm
# car should turn right but stay in position
# the put another obstacle in front of car
# use to test angle, etc.
# to be deleted later
import time

import picar_4wd as fc

speed = 5 #super slow please
distance = 25

def main():
    test_round = 1
    while True:
        #print(f"round {test_round} begins")
        scan_list = fc.scan_step(distance) #try 25 centimeter
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(f"This is tmp: {tmp}")
        print(f"This is scan_list: {scan_list}")
        if tmp != [2,2,2,2]:
            fc.turn_right(speed)
            time.sleep(1)
            fc.stop()
        else:
            pass
        print(f"Next round in 3 seconds")
        time.sleep(3) # buy me some time to reset my obstacles
        test_round += 1


if __name__ == "__main__":
    try:
        print("Start")
        main()
    finally:
        fc.stop()
