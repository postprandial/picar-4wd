# Testing increasing power increments for straight ahead
# interrupt using enter or control C
import picar_4wd as fc
import time, sys, select

power = 30

while True:
    print(f"forward with {power} power")
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = input()
        break
    fc.forward(power)
    fc.stop()
    time.sleep(3)
    power += 5
    if power == 25:
        power = 0

fc.stop()
print("All done")
