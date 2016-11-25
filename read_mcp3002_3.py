#!/usr/bin/env python3
###
### read MCP3002 ADC analog value via RasPi SPI
###

import wiringpi2 as wp
import time
import requests
from datetime import datetime

# SPI channle (0 or 1)
SPI_CH = 0

# pin base (above 64)
PIN_BASE=70

# GPIO number
LED_PIN = 25

# threshold
THRESHOLD = 200

# setup
wp.mcp3002Setup (PIN_BASE, SPI_CH)
wp.wiringPiSetupGpio()
wp.pinMode(LED_PIN, wp.GPIO.OUTPUT)

# if a sensor value is over THRESHOLD,
# flash led.
while True:
    value = wp.analogRead(PIN_BASE)
    print (value)

    if value > THRESHOLD:
      wp.digitalWrite(LED_PIN, wp.GPIO.HIGH)
      time.sleep(0.2)
      wp.digitalWrite(LED_PIN, wp.GPIO.LOW)
      time.sleep(0.2)
      requests.post("https://sb9is9g79e.execute-api.ap-northeast-1.amazonaws.com/prod/sample2", json={"key1": datetime.now().strftime("%Y%m%d"),"key2": value}) 
    time.sleep(1)
