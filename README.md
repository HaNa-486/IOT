# IOT
## how to setup Raspbian (如何安裝Raspbian)
利用noobs安裝請參考此連結:https://sites.google.com/site/raspberypishare0918/home/di-yi-ci-qi-dong/noobs-an-zhuang

## dht-22 setup (溫溼度檢測儀)
參考此連結:https://www.rototron.info/dht22-tutorial-for-raspberry-pi/

我用的是"pigpiod"這個library

備註:程式碼中用到的GPIO都是 GPIO.BCM的形式

## PIR Motion Sensor (紅外線感測器)
請參考此連結:https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio

備註:為了我程式的方便性，我把我自己程式碼中的GPIO的號碼形式改成 GPIO.BCM

## Pi Camera
請參考此連結:https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4

備註:請在樹梅派關機的時候連結攝像頭與樹莓派

## Remote control (一個樹梅派控制另一個樹梅派)
請參考此連結:https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

備註:要利用此功能必須處於同一個網域下 (白話文，要連結同一個wifi 或是 路由器)




(camera + dht-22 + PIR sensor) video link1 : https://drive.google.com/open?id=1HklNJhrj0_w72Bfc6g0L1A2p__B1yKky

((camera + PIR sensor + remote control feature) video link2 : https://drive.google.com/open?id=1qIbD3HEuomEHmv1ogZKc4FTZCsjuT0TM
