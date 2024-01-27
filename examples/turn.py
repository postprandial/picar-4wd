import picar_4wd as fc
import time, sys, select

power = 25

while True:
    print(f"turning with {power} speed for 1 second: starting in 2 seconds")
    time.sleep(2)
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = input()
        break
    fc.turn_right(power)
    time.sleep(1)
    fc.stop()
    # power += 5
    if power == 25:
        power = 0

fc.stop()
print("All done")