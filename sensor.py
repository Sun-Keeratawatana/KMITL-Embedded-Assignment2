import machine
import utime

touch_pin_no = 0
water_pin_no = 2
pir_pin_no = 1

touch_signal = machine.Pin(touch_pin_no, machine.Pin.IN)
water_signal = machine.Pin(water_pin_no, machine.Pin.IN)
pir_signal = machine.Pin(pir_pin_no, machine.Pin.IN)

while True:
    if touch_signal.value():
        print("Touch sensor activated at ", str(utime.localtime()[:-2]))
    if water_signal.value():
        print("Water detected at", str(utime.localtime()[:-2]))
    if pir_signal.value():
        print("Motion detected at ", str(utime.localtime()[:-2]))
    utime.sleep(1)
