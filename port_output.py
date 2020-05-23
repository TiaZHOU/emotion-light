import serial

try:
    # GNU / Linux/ dev / ttyUSB0 or Windows COM5
    portx = "COM5"
    # ：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    bps = 9600
    # None：always waiting，0  immediately， seconds
    timex = 5
    # open port
    ser = serial.Serial(portx, bps, timeout=timex)
    # write data
    result = ser.write("0 233 0".encode())
    print("total:", result)
    ser.close()  # close port
except Exception as e:
    print("---exception---：", e)
