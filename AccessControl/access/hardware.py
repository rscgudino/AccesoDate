import serial

def read_card():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    card_id = ser.readline().strip()
    ser.close()
    return card_id

def control_door(door_id, action):
    # Enviar comando para abrir/cerrar puerta
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    command = f"{door_id}:{action}"
    ser.write(command.encode())
    ser.close()
