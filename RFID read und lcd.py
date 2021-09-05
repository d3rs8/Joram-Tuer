#!/usr/bin/env python



import RPi.GPIO as GPIO
import drivers
from datetime import datetime
import time
from subprocess import check_output

from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)

display = drivers.Lcd()

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)


reader = SimpleMFRC522()


text1 = "Kein Zugriff!"


    
while True:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.IN)
        if GPIO.input(16) == 0:
                try:

                        while True:
                            GPIO.setmode(GPIO.BCM)
                            GPIO.setup(23, GPIO.OUT)
                            GPIO.setup(24, GPIO.OUT)
                            GPIO.output(24, GPIO.HIGH)
                            GPIO.output(23, GPIO.LOW)
            
                            id, text = reader.read()
            
                            def clear():
                                time.sleep(5)
                                GPIO.output(23, GPIO.LOW)
                                GPIO.output(24, GPIO.LOW)
                                display.lcd_clear()
                
                            def exept():
                                display.lcd_display_string(str(text), 1)
                                display.lcd_display_string('ID:' + str(id), 2)
                                print(id)
                                print(text)
                        
                                clear()
            
                            def error():
                                print("Kein Zugriff!")
                                display.lcd_display_string('  Kein Zugriff!', 1)
                                display.lcd_display_string('  Kein Zugriff!', 2)
                                GPIO.output(24, GPIO.HIGH)
                                GPIO.output(23, GPIO.LOW)
                                clear()
                
                            tr = 1075761060547
                            card3 = 564790171908
                            text2 = text
                            tro = 4

                            if GPIO.input(16) == 0:
                                    print("1")
                            else:
                                    print("0")
                            if text == '':
                                text = "Error"
        
                            if id == 1075761060547 or card3:
                
                                if id == tr:
                                    id = " T. Redlich"
                                    GPIO.output(23, GPIO.HIGH)
                                    GPIO.output(24, GPIO.LOW)
                                    exept()

                                elif id == card3:
                                        id = "Guest"
                                        GPIO.output(23, GPIO.HIGH)
                                        GPIO.output(24, GPIO.LOW)
                                        exept()
                

                                else:
                                        error()

                except KeyboardInterrupt:
    
    
        
                        GPIO.cleanup()
                        print("Cleaning up!")
                        display.lcd_clear()
                        break

        else:
                print("Break")
                display.lcd_display_string('  Alarm!', 1)
                display.lcd_display_string('  Alarm!', 2)
                
                for i in range(10):
                        GPIO.output(23, GPIO.LOW)
                        time.sleep(0.1)
                        GPIO.output(23, GPIO.HIGH)
                        time.sleep(0.1)

                time.sleep(23)
                display.lcd_clear()
                

                  
                        
