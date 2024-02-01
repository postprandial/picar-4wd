# Drives car autonomously per Lab 1A specifications
# to be removed later: contains print statements for debugging & verbose comments

import picar_4wd as fc
import time, random

power = 5 # slow for driving forward and backward.
turn_power = 20 # faster for turning
distance = 35 # argument for scan_step below so ultrasonic module looks for obstacles up to 35 cm

# note on speed vs power: example scripts call the parameter for fc.forward, etc. alternatingly power or speed
# I'll use power to distinguish it from the Speed class in the __init__


def random_direction(min_time = 1, max_time = 2):
    """picks left or right and time period between min_time and max_time seconds for turning"""
    turns = [fc.turn_left, fc.turn_right]
    turn_duration = random.uniform(min_time, max_time)
    turn_direction = turns[random.randint(0,1)]
    return turn_direction, turn_duration


def main():
    test_round = 1
    while True:
        print(f"round {test_round} begins")
        fc.forward(power)
        scan_list = fc.scan_step(distance)
        # scan_step returns a list containing max_angle/STEP number of samples from the ultrasonic module taken
        # every STEP degrees (for a ANGLE_RANGE field).
        # It looks for obstacles that are up to "distance" centimeters away
        if not scan_list:
            continue

        # grab center 4 samples from scan_list with even number of samples (5 samples if odd number)
        scan_list_size = int(len(scan_list))
        start_sample, end_sample = (scan_list_size//2 - 2), (scan_list_size//2 + 2) # indices to slice "center samples"
        no_obstacles = [2 for i in scan_list[start_sample: end_sample]]
        # no_obstacles is what "tmp" would look like if no obstacles were detected
        # 2 means "no obstacles"
        # 1 means "obstacles between outer boundary ref1 and near boundary ref2 cm - close but not yet too close
        # 0 means "obstacles between ref2 and car's nose" -  very close.
        tmp = scan_list[start_sample:end_sample] # these are the center samples we're actually evaluating for obstacles

        print(f"This is tmp: {tmp}")
        print(f"This is no_obstacles: {no_obstacles}")
        print(f"This is scan_list: {scan_list}")

        if tmp != no_obstacles:
            fc.backward(power)
            time.sleep(1) # decreased sleep increase speed for forwards
            # picks random new direction
            turn_this_way, duration = random_direction(1,2)
            turn_this_way(turn_power) # this is faster for obvious reasons
            time.sleep(duration) # duration is how long it spins
            fc.stop()

        test_round += 1


if __name__ == "__main__":
    try:
        print("Start")
        main()
    finally:
        fc.stop()
