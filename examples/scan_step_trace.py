# for debugging and tracing scan_step function (in __init__, for ultrasonic module)
# VERIFY: that servo returns to angle 0 before it starts taking samples.
# print out: current angle, scan_list, STEP (to see if we've started reversing things)
# PLACE obstacle closer than 35 centimeters right at 0 degrees.
# NO MOVEMENT. IT STAYS ON THE TABLE.

import time

import picar_4wd as fc

speed = 5 # slow
distance = 35 # for scan_step

def main():
    print(f"Start")
    test_round = 1
    while True:
        print(f"round {test_round} begins")
        scan_list = fc.scan_step(distance)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(f"This is tmp: {tmp}")
        print(f"This is scan_list: {scan_list}")
        if tmp != [2,2,2,2]:
            time.sleep(1)
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