# this file will have a basic function

import datetime
from time import sleep

def print_time():
    print(f"Today is {datetime.datetime.now()}")


def main():
    print_time()


if __name__ == '__main__':
    print("Program is starting... \n")
    sleep(3)
    main()
    sleep(3)
    print("\n Program is complete")