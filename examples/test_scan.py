# modification of obstacle_avoidance
# to be deleted later
import picar_4wd as fc

speed = 5 #super slow please

def main():
    while True:
        scan_list = fc.scan_step(25) #try 25 centimeter
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(f"This is tmp: {tmp}")
        print(f"This is scan_list: {scan_list}")
        if tmp != [2,2,2,2]:
            fc.turn_right(speed)
        else:
            fc.forward(speed)


if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
