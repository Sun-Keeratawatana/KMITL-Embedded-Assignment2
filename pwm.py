import machine
import utime

Pwm = machine.PWM(machine.Pin(15))
Pwm.freq(1000)
for i in range(2):
    for duty in range(65535):
        Pwm.duty_u16(duty)
    utime.sleep(1)
    for duty in range(65536, -1, -1):
        Pwm.duty_u16(duty)
    utime.sleep(1)
