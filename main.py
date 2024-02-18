
# 7セグLED表示
import machine
import time


LED7SEG[0] = 0b00000011
LED7SEG[1] = 0b10011111
LED7SEG[2] = 0b00100101
LED7SEG[3] = 0b00001101
LED7SEG[4] = 0b10011001
LED7SEG[5] = 0b01001001
LED7SEG[6] = 0b01000001
LED7SEG[7] = 0b00011111
LED7SEG[8] = 0b00000001
LED7SEG[9] = 0b00001001

def ledview(value):
    ser = machine.Pin(16, machine.Pin.OUT)
    rclk = machine.Pin(17, machine.Pin.OUT)
    srclk = machine.Pin(18, machine.Pin.OUT)

    ser.value( 0 )
    rclk.value( 0 )
    srclk.value( 0 )

    for i in range(8):
        srclk.value( 0 )
        time.sleep_ms(10)
        v = LED7SEG[value] & (1 << i)
        ser.value( v )
        time.sleep_ms(10)
        srclk.value( 1 )
        time.sleep_ms(10)
    rclk.value( 1 )
    time.sleep_ms(10)
    rclk.value( 0 )

ledview(7)
time.sleep(1)
print("END")
    

    