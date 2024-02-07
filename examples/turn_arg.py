import picar_4wd as fc
import time, sys, select
import sys

power = 50
duration = sys.argv[1]

while True:
    print(f"turning with {power} speed for {duration} second: starting in 2 seconds")
    time.sleep(2)
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = input()
        break
    fc.turn_right(power)
    time.sleep(duration)
    fc.stop()
    # power += 5
    # if power == 40:
    #    power = 5

fc.stop()
print("All done")