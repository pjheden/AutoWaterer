from datetime import datetime
import time

# Time between each time we should water
water_time_treshold = 60*60 # seconds
# Time the pump should be on
pump_time = 1 # seconds

def start_pump():
    '''
    Starts the water pump
    '''
    print("Pump started")

def stop_pump():
    '''
    Stops the water pump
    '''
    print("Pump stopped")

def pump():
    '''
    Pumps water for {pump_time} and then stops
    '''
    start_pump()
    time.sleep(pump_time)
    stop_pump()

def auto_water():
    '''
    Initiates the automatic service
    '''

    # Idea: Compare now to last time we watered
    # and water if its above some treshold
    try:
        while 1:
            pump()
            time.sleep(water_time_treshold)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        stop_pump() # Make sure the pump is stopped
        # GPIO.cleanup() # cleanup all GPI

if __name__ == '__main__':
    auto_water()
