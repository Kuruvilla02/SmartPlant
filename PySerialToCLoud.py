import serial  # using serial library
import datetime  # using date time library
import urllib3  # using URL library


ser = serial.Serial('COM5', 9600)  # open serial port, change to yours! #object ser
ser.flushInput()  # method
baseURL = 'https://api.thingspeak.com/update?api_key='  # base Thingspeak URLAPI_key=
API_key = 'K8ZLCA9UWXGD9RX5'  # use your own Write

while True:

    # try:
    ser_bytes = ser.readline()  # read one line from serial port #method
    decoded_bytes = ser_bytes[0:len(ser_bytes) - 2].decode("utf-8")  # and grab the data
    ser_bytes2 = ser.readline()  # method
    decoded_bytes2 = ser_bytes2[0:len(ser_bytes2) - 2].decode("utf-8")
    ser_bytes3 = ser.readline()  # read one line from serial port #method
    decoded_bytes3 = ser_bytes[0:len(ser_bytes) - 2].decode("utf-8")  # and grab the data
    ser_bytes4 = ser.readline()  # method
    decoded_bytes4 = ser_bytes2[0:len(ser_bytes2) - 2].decode("utf-8")
    now = datetime.datetime.now()  # create timestamp #object and method
    now = now.strftime("%Y-%m-%d %H:%M:%S")  # put on readable format method

    data = ("'{}','{},'{}','{}',{},\r\n".format(now, decoded_bytes, decoded_bytes2, decoded_bytes3, decoded_bytes4))  # prepare data to print
    print(data)


    value_m = int(decoded_bytes)
    value_l = int(decoded_bytes2)
    value_t = int(decoded_bytes3)
    value_h = int(decoded_bytes4)



    tsURL = ("{}{}&field1={}&field2={}&field3={}&field4".format(baseURL, API_key, value_m, value_l, value_t, value_h))
    http = urllib3.PoolManager()  # object http
    # # sending HTTP request to Thingspeak
    tspeak = http.request('GET', tsURL)  # method

