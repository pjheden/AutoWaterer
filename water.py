from datetime import datetime
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

def init_output(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)
    
# Time between each time we should water
water_time_treshold = 60*60 # seconds
# Time the pump should be on
pump_time = 0.1 # seconds

def start_pump(pump_pin):
    '''
    Starts the water pump
    '''
    GPIO.output(pump_pin, GPIO.LOW)
    print("Pump started")

def stop_pump(pump_pin):
    '''
    Stops the water pump
    '''
    GPIO.output(pump_pin, GPIO.HIGH)
    print("Pump stopped")

def pump(pump_pin):
    '''
    Pumps water for {pump_time} and then stops
    '''
    start_pump(pump_pin)
    time.sleep(pump_time)
    stop_pump(pump_pin)

def auto_water():
    '''
    Initiates the automatic service
    '''
    pump_pin = 7
    init_output(pump_pin)
    
    try:
        while 1:
            pump(pump_pin)
            time.sleep(water_time_treshold)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        stop_pump() # Make sure the pump is stopped
        # GPIO.cleanup() # cleanup all GPI

if __name__ == '__main__':
    auto_water()
