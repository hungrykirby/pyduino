import serial
import re
import arrange

def main():
    with serial.Serial('COM3',9600,timeout=0.1) as ser:
        arra = arrange.Arrange(ser)
        try:
            while True:
                c = ser.readline()
                de = c.decode('utf-8')
                m = re.match("\-*[\w]+", str(de))
                if(m != None):
                    #print(m.group())
                    arra.fetch_three_numbers(m.group())
                else:
                    pass
                    #print(type(m))
        except KeyboardInterrupt:
            ser.close()
        ser.close()


if __name__ == "__main__":
    main()
