import RPi.GPIO as GPIO
from gpiozero import Motor, LED, OutputDevice
from time import sleep

# # led = LED(17)
print('motozero_move')
motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)
print('motozero_move motor1_enable', motor1_enable)
# motor2 = Motor(6, 22)
# motor2_enable = OutputDevice(17, initial_value=1)
# motor3 = Motor(23, 16)
# motor3_enable = OutputDevice(12, initial_value=1)
# motor4 = Motor(13, 18)
# motor4_enable = OutputDevice(25, initial_value=1)

# motor1.forward()

# motors = (motor1, motor2, motor3, motor4)

# for motor in motors:
#     motor.forward()
#     print(motor.value)
#     # led.on()
#     sleep(1)
#     motor.stop()
#     # motor.pause()




# while True:
#     led.on()
#     sleep(1)
#     led.off()
#     sleep(1)


#  # Import GPIO
# import RPi.GPIO as GPIO

# # Import sleep
# from time import sleep

# # Set the GPIO mode
# GPIO.setmode(GPIO.BCM)

# # Define GPIO pins
# Motor1A = 27
# Motor1B = 24
# Motor1Enable = 5

# # Set up defined GPIO pins
# GPIO.setup(Motor1A,GPIO.OUT)
# GPIO.setup(Motor1B,GPIO.OUT)
# GPIO.setup(Motor1Enable,GPIO.OUT)
# # We then tell the code to turn certain pins on or off to make the motor move:
# # Turn the motor on
# GPIO.output(Motor1A,GPIO.HIGH) # GPIO high to send power to the + terminal
# GPIO.output(Motor1B,GPIO.LOW) # GPIO low to ground the - terminal
# GPIO.output(Motor1Enable,GPIO.HIGH) # GPIO high to enable this motor

# # Leave the motor on for 3 seconds
# sleep(3)

# # Stop the motor by 'turning off' the enable GPIO pin
# GPIO.output(Motor1Enable,GPIO.LOW)

#  # Always end this script by cleaning the GPIO
# GPIO.cleanup() 