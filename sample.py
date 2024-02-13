# from machine import Pin
# import utime
# p = Pin(25)
# p.init( Pin.OUT )
# v = False

# while( True ):
#     p.value( v )
#     v = not v
#     utime.sleep(0.5)


import machine
import time

# ADCを行うピンの設定です。
# GP28(ADC2)を使用します
cds = machine.ADC(0)

# 16bitの数値一単位での電圧値を設定します
unit = 0.00005035477

# 電圧値を100回読み込みます
for i in range(100):
    
    # ADCの値を読み込みます(16bitの生の数値)
    voltRaw = cds.read_u16()
    
    # 生値を表示します
    print("voltRaw:" + str(voltRaw))
    
    # 16bitの値から、電圧値に変換します
    volt = voltRaw * unit
    
    # 電圧値を表示します(:.3fは少数点以下3桁を表示する設定です)
    print( "volt:" + "{:.3f}".format(volt))
    
    # 1秒待機します
    time.sleep(10)
