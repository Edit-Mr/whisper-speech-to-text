import serial

# Open the serial port
ser = serial.Serial('COM10', 115200)

ser.write(b'Hello\n')

while True:
    received_text = ser.read_all().decode('utf-8')
    print(received_text)
    if received_text == 'start':
        ser.write(b'alright\n')
        break

ser.close()
