from RPi import GPIO
from firebase import firebase
from time import sleep

url = 'https://helloworld-8cf45.firebaseio.com/' # URL to Firebase database
token = 'YW3EBnf50kQ3dAbhsoeaIMy0poFDKe3R1TP6BWAm' # unique token used for authentication

firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'green':23, 'red':24}
leds = [23, 24]

GPIO.setup(leds, GPIO.OUT)





def set_led(ledno, status):
    # you can use this to set the LED on or off
    if status == 'on':
        GPIO.output(ledno, GPIO.HIGH)
    else:
        GPIO.output(ledno, GPIO.LOW)

while True:
    # get firebase data and call setLED
    ls = firebase.get('/state_list')
    
    if ls != None:
        set_led(23,ls[0])
        set_led(24,ls[1])
    sleep(0.5)