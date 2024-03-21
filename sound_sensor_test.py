import serial

arduino_port = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate)

while True:
    data = ser.readline().decode('utf-8').strip()

    print("data:", data)
