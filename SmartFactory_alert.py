
import time
import serial
import paho.mqtt.client as mq
import ssl
s=serial.Serial('/dev/ttyACM0',9600) # define ports in linux
c=mq.Client()
rootca=r'/home/pi/Desktop/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem.txt'
keyfile=r'/home/pi/Desktop/61b07b1835-private.pem.key'
certfile=r'/home/pi/Desktop/61b07b1835-certificate.pem.crt'
c.tls_set(rootca,keyfile=keyfile,certfile=certfile,cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1_2,ciphers=None)

while True:
	data=s.readline()
	data=data.decode() # Decode from bytes format to raw format
	data=data[:-2]
	print(data)
	c.connect('az0gt492bl7sp.iot.us-east-1.amazonaws.com',8883)
	time.sleep(1)
	c.publish('iot/today','{"temp":'+data+'}') #json format
	c.disconnect()
	time.sleep(5)
