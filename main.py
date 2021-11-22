#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Nov 2021
# Grandmother A


def main():
    # main function for grandmother A

    # asking for input
    try:
        age = input("Please enter your age: ")
        age = int(age)

        # process/output
        if age > 40 or age < 25:
            print("You are NOT an acceptable age")
        else:
            print("You are an appropriate age")
    except ValueError:
        print("Input has to be integer")

    # done
    print("\nDone.")


if __name__ == "__main__":
    main()
