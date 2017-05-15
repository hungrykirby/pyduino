import serial
import re
import threading
import sys

import arrange

c = "xx"
console_input = sys.argv
print(len(console_input))
if len(console_input) == 2 and (console_input[1] == "test" or console_input[1] == "train"):
    MODE = console_input[1]
else:
    sys.exit()


def serial_loop():
    with serial.Serial('COM3',9600,timeout=0.1) as ser:
        arra = arrange.Arrange(ser, MODE)
        try:
            while True:
                s = ser.readline()
                de = s.decode('utf-8')
                m = re.match("\-*[\w]+", str(de))
                if(m != None):
                    #print(m.group())
                    arra.fetch_three_numbers(m.group(), c)
                else:
                    pass
                    #print(type(m))
        except:
             print("Unexpected error:", sys.exc_info()[0])
             raise
        ser.close()

ser_loop = threading.Thread(target=serial_loop,name="ser_loop",args=())
ser_loop.setDaemon(True)
ser_loop.start()

def main():
    global c
    while True:
        tmp = input()
        if c != tmp:
            c = tmp
            print("c =", c)
        else:
            pass
        if tmp == 'a':
            sys.exit()



if __name__ == "__main__":
    main()
