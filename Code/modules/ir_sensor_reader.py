import RPi.GPIO as GPIO

# IR sensor pins
IR_PINS = [26, 17, 27, 22, 23, 24, 4]

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
for pin in IR_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor

def read_ir_sensors():
    """
    Reads the states of all 7 IR sensors and returns the triggered sensor number.
    If more than one sensor is triggered, returns None.
    
    Returns:
        int or None: The number of the triggered IR sensor (1-7), or None if no/invalid sensors are triggered.
    """
    triggered_sensors = []

    for index, pin in enumerate(IR_PINS):
        if GPIO.input(pin) == GPIO.LOW:  # Triggered when the sensor reads LOW
            triggered_sensors.append(index + 1)  # Store the sensor number (1-based)

    if len(triggered_sensors) == 1:
        return triggered_sensors[0]  # Return the single triggered sensor number
    else:
        return None  # No sensors or more than one sensor triggered
