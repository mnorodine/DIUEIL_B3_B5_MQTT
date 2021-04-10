#
#
# Ce module contient une fonction global SensorRed()


from machine import Pin
import onewire
import ds18x20
import time
 
#ow = onewire.OneWire(Pin(14))
#sensor = ds18x20.DS18X20(ow)
#roms = sensor.scan()

#print('Numéro de série ROM : ',end='')
#for el in roms[0]:
#    print('{:02X}'.format(el),end='')
#print()

#while True :
#    sensor.convert_temp()
#    time.sleep(1)
#    print(sensor.read_temp(roms[0]))


class Sensors:

    def __init__(self, func_count):
    	self.func_count = func_count 
    	self.FUNC_ID 	= 0
    	self.rsp		= "Null"

    def ReadSensorDS18B20(self):
        ow = onewire.OneWire(Pin(14))
        sensor = ds18x20.DS18X20(ow)
        roms = sensor.scan()

    	#self.rsp = "Sensor 1"
        sensor.convert_temp()
        time.sleep(1)
        self.rsp = sensor.read_temp(roms[0])
    	

    def ReadSensor_2(self):
    	self.rsp = "Sensor 2"

    def ReadSensor_3(self):
    	self.rsp = "Sensor 3"

    def ReadSensor_4(self):
    	self.rsp = "Sensor 4"

    def ReadSensor_5(self):
    	self.rsp = "Sensor 5"

    def Read(self):
    	if (self.FUNC_ID == 0):
    		self.ReadSensorDS18B20()
    	else:
    		if (self.FUNC_ID == 1):
    			self.ReadSensor_2()
    		else:
    			if (self.FUNC_ID == 2):
    				self.ReadSensor_3()
    			else:
    				self.rsp = "Null"

    	self.FUNC_ID += 1
    	if (self.FUNC_ID >= self.func_count):
    		self.FUNC_ID = 0

    	return self.rsp