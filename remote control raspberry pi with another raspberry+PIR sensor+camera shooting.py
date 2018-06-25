from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO.BCM 選項是指定GPIO後面的號碼
GPIO.setup(17, GPIO.IN)

factory = PiGPIOFactory(host='192.168.0.101')
led = LED(4, pin_factory=factory)



while True:
    i=GPIO.input(17)
    if i == 1:
        print("attention, camera shoot a photo")
        camera = PiCamera()
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.close()
        print("camera shot down and blink a led on another raspberry pi")
        led.on()
        sleep(5)
        led.off()
        print("exit the loop and wait for next IR change")
        print("")
        sleep(0.5)
        
    elif i == 0:
        sleep(0.5)


