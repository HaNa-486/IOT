import pigpio
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO.BCM 選項是指定GPIO後面的號碼
GPIO.setup(17, GPIO.IN)
pi = pigpio.pi()
import DHT22
s = DHT22.sensor(pi, 12)




while True:
    i=GPIO.input(17)
    if i == 1:
        print("attention")
        camera = PiCamera()
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.close()
        sleep(3)
        s.trigger()
        sleep(5)
        print("GG")
        print('{:3.2f}'.format(s.humidity() / 1.))
        print('{:3.2f}'.format(s.temperature() / 1.))
        
        sleep(0.5)
        
    elif i == 0:
        s.cancel()
        sleep(0.5)

pi.stop()