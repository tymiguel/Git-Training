# this file will have a basic function

import datetime
from my_package import code_sugar


def print_time():
    print(f"Today is {datetime.datetime.now()}")


def main():
    code_sugar.start_program()
    print_time()
    code_sugar.end_program()


if __name__ == '__main__':
    main()