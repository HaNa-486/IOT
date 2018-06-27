#為了讓dht-22能運作，我把程式碼儲存在pigpiod那個資料夾裡
#經過我多次的嘗試與修正，dht-22有時候會因為某種硬體上的原因，導致無法偵測數據
import pigpio
from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #GPIO.BCM 選項是指定GPIO後面的號碼
GPIO.setup(17, GPIO.IN) #把PIR sensor 連接的GPIO 17號設為輸入端
pi = pigpio.pi()
import DHT22
s = DHT22.sensor(pi, 12) #dht-22的data由GPIO 12號傳入給樹梅派




while True:
    i=GPIO.input(17)
    if i == 1:  #當PIR sensor 有接收到變化並產生一個電流給 GPIO 17 
        print("attention")
        camera = PiCamera() 
        camera.capture('/home/pi/Desktop/image.jpg') #拍一張照片存在桌面上
        camera.close()
        sleep(3)
        s.trigger() #讓溫溼度儀 偵測，並傳回資料給樹莓派
        sleep(5)
        print("GG")
        print('{:3.2f}'.format(s.humidity() / 1.))
        print('{:3.2f}'.format(s.temperature() / 1.))
        
        sleep(0.5)
        
    elif i == 0:  #當紅外線感測器沒有接收到變化時
        s.cancel()
        sleep(0.5)

pi.stop()
