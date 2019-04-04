# -*- coding:utf-8 -*-
import sys
import time
import Adafruit_DHT as dht
import os
import requests
import json

sensor = dht.DHT11

pin = 4

buf1 = 0


def waitingforchange():

	while True:

	        humidity2, temp2 = dht.read_retry(sensor, pin)

       		if temp is not None and humidity2 is not None:

                	print 'Humidity={0:0.1f}%'.format(humidity2)

			global buf1

                	buf2 = buf1 - humidity2

                	if buf2 > 10 :

                        	now = time.localtime()

                        	s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

                        	print s

                        	myhost = os.uname()[1]

                        	print myhost

                        	print "기저귀 교체완료"

				url = "http://192.168.0.5:8080/hanggies/change"
                        	data =  {'sid': myhost, 'signal': 'change'}
                        	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                        	res = requests.post(url, data=json.dumps(data), headers=headers)

				break

			buf1 = humidity2

			time.sleep(2)

		else: print "can't get sensor data!"




while True:

        humidity, temp = dht.read_retry(sensor, pin)

        if temp is not None and humidity is not None:

		os.system('clear')

		print 'Temp={0:0.1f}*C'.format(temp)

		print 'Humidity={0:0.1f}%'.format(humidity)

		buf2 = humidity - buf1

		if buf2 > 10 and buf2 < 30 :

			now = time.localtime()

			s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

			print s

			myhost = os.uname()[1]

			print myhost

			print "기저귀를 교체해주세요!"

			url = "http://192.168.0.5:8080/hanggies/sensing"
			data =  {'sid': myhost, 'signal': 'sensing'}
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			res = requests.post(url, data=json.dumps(data), headers=headers)

			print res

			waitingforchange()

		buf1 = humidity

                time.sleep(2)

        else: print "Can't get sensor data!"
