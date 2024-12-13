import RPi.GPIO as GPIO
import time
from limit_switch_reader import read_limit_switches

# GPIO pin configuration
STEP_PIN = 16       # Step control
DIR_PIN = 20        # Direction control
ENABLE_PIN = 21     # Enable motor

DELAY = 0.0001  # Delay between steps

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Function to move the motor
def move_motor(direction, steps):
    """
    Move the gantry cart in the specified direction for a given number of steps.
    
    Parameters:
        direction (str): 'left' or 'right'
        steps (int): Number of steps to move
    """
    GPIO.output(ENABLE_PIN, GPIO.LOW)  # Enable the motor driver

    # Set direction
    if direction == 'left':
        GPIO.output(DIR_PIN, GPIO.HIGH)
    elif direction == 'right':
        GPIO.output(DIR_PIN, GPIO.LOW)
    else:
        print("Invalid direction! Use 'left' or 'right'.")
        return

    # Step the motor
    for step in range(steps):
        # Check limit switches
        left_switch, right_switch = read_limit_switches()
        if direction == 'left' and left_switch:
            print("Limit switch LEFT triggered! Stopping.")
            break
        elif direction == 'right' and right_switch:
            print("Limit switch RIGHT triggered! Stopping.")
            break

        # Generate step pulse
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(DELAY)

    GPIO.output(ENABLE_PIN, GPIO.HIGH)  # Disable the motor driver