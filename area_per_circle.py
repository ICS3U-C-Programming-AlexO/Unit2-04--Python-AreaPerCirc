#!/usr/bin/env python3
# Created by: Alex OBrien
# Created on: September 30, 2026
# This program calculates the area and circumference of a circle
# by asking the user for the radius
import math


def main():
    # prompt user for the radius of the circle in cm
    radius_input = input("Enter the radius of your circle (cm): ")
    radius = float(radius_input)

    # Calculate circumference & area
    circumference = 2 * math.pi * radius
    area = math.pi * (radius**2)

    # Display results formatted to 2nd decimal point
    print("The Circumference and the Area are:")
    print(f"Circumference: {circumference:.2f}cm")
    print(f"Area: {area:.2f}cm²")


if __name__ == "__main__":
    main()
