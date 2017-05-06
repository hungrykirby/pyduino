import serial
import re

def main():
    with serial.Serial('COM3',9600,timeout=1) as ser:
        while True:
            c = ser.readline()
            de = c.decode('utf-8')
            m = re.match("\-*\d+", str(de))
            if(m != None):
                print(m.group())
            else:
                pass
                #print(type(m))
        ser.close()

if __name__ == "__main__":
    main()
