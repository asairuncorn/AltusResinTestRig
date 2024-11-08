from time import sleep
import Adafruit_ADS1x15

def pressure_sensor_1():
    adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

#Gain = 2/3 for reading voltages from 0 to 6.144V.
#See table 3 in ADS1115 datasheet
    GAIN = 2/3

#Main loop.
    while True:
        value = [0]
# Read ADC channel 0
        value[0] = adc.read_adc(0, gain=GAIN)
# Ratio of 15 bit value to max volts determines volts
        volts = value[0] / 32767.0 * 6.144
# Tests shows linear relationship between psi & voltage:
        psi = 50.0 * volts - 25.0
# Bar conversion
        bar = psi * 0.06894757

        print("Voltage: {0:0.3f}V, PSI: {1:0.0f}, Bar: {2:0.1f}".format(volts, psi, bar))

        sleep(1)
        return psi