#edited from move_forward to measure how power translates into velocity

import picar_4wd as fc
import time
import sys

power = sys.argv[1]

print(f"going forward with power: {power}")

try:
    while True:
        fc.forward(power)
        time.sleep(1)
finally:
    fc.stop()
    time.sleep(0.2)

    