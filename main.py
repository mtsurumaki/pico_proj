
# 7セグLED表示
import machine
import time

LED7SEG = [0] * 10
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

# def init():
ser = machine.Pin(16, machine.Pin.OUT)
rclk = machine.Pin(17, machine.Pin.OUT)
srclk = machine.Pin(18, machine.Pin.OUT)

digit0 = machine.Pin(11, machine.Pin.OUT)
digit1 = machine.Pin(12, machine.Pin.OUT)
digit2 = machine.Pin(13, machine.Pin.OUT)
digit3 = machine.Pin(14, machine.Pin.OUT)

cds = machine.ADC(0)

# 16bitの数値一単位での電圧値を設定します
unit = 0.00005035477

# ADCの値を読み込みます(16bitの生の数値)
voltRaw = cds.read_u16()

# 16bitの値から、電圧値に変換します
volt = voltRaw * unit

# value :表示する値
# ser   :シリアルPIN
# rclk  :ラッチPIN
# srclk :クロックPIN
# digit :表示桁の有効PIN
# piriod:"."の有無
def ledview(value, ser, rclk, srclk, digit, piriod):
    ser.value( 0 )
    rclk.value( 0 )
    srclk.value( 0 )

    if piriod != False:
        v = (LED7SEG[value] & 0b11111110)
    else:
        v = LED7SEG[value]
        
    for i in range(8):
        srclk.value( 0 )
        bit = v & (1 << i)
        ser.value(bit)
        srclk.value( 1 )
    rclk.value( 1 )
    rclk.value( 0 )
    digit.value(1)
    time.sleep_ms(2)
    digit.value(0)

for i in range(1000):
    ledview((int)((volt/0.001)%10), ser, rclk, srclk, digit0, False)
    ledview((int)((volt/0.01)%10), ser, rclk, srclk, digit1, False)
    ledview((int)((volt/0.1)%10), ser, rclk, srclk, digit2, False)
    ledview((int)(volt/1), ser, rclk, srclk, digit3, True)

print(volt)
print("END")
