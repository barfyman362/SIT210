import RPi.GPIO as GPIO 
import time  

LED_PIN = 19

GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(False)  

GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.output(LED_PIN, GPIO.LOW)  

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) 
        time.sleep(0.25)  
        GPIO.output(LED_PIN, GPIO.LOW) 
        time.sleep(0.25)  

except KeyboardInterrupt:
    GPIO.cleanup()  
