# Drives car autonomously per Lab 1A specifications
# to be removed later: contains print statements for debugging & verbose comments

import picar_4wd as fc
import time, random

power = 10
turn_power = 50
distance = 35


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

        if not scan_list:
            continue

        scan_list_size = int(len(scan_list))
        start_sample, end_sample = (scan_list_size//2 - 3), (scan_list_size//2 + 2)
        no_obstacles = [2 for i in scan_list[start_sample: end_sample]]

        tmp = scan_list[start_sample:end_sample]

        if tmp != no_obstacles:
            fc.backward(power)
            time.sleep(1)
            turn_this_way, duration = random_direction(1,1.5)
            turn_this_way(turn_power)
            time.sleep(duration)
            fc.stop()

        test_round += 1

if __name__ == "__main__":
    try:
        print("Start")
        main()
    finally:
        fc.stop()
