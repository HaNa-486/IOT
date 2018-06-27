#與另一個程式碼相同的部分就不再重複註解
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.IN)

#remote control 特別需要的library及設定
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory(host='192.168.0.101') #id位置請查看另一台樹梅派的ip
led = LED(4, pin_factory=factory) #把LED與GPIO 4連接



while True:
    i=GPIO.input(17)
    if i == 1:
        print("attention, camera shoot a photo")
        camera = PiCamera()
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.close()
        print("camera shot down and blink a led on another raspberry pi")
        led.on() #當裝有PIR sensor的樹莓派接收到紅外線的變化後，另一台樹莓派的LED燈就亮了
        sleep(5)
        led.off()
        print("exit the loop and wait for next IR change")
        print("")
        sleep(0.5)
        
    elif i == 0:
        sleep(0.5)


