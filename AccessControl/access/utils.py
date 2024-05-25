# utils.py
from .models import Person, Door, AccessLog
import serial
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def read_card():
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    card_id = ser.readline().strip()
    ser.close()
    return card_id

def control_door(door_id, action):
    ser = serial.Serial('/dev/ttyUSB1', 9600)
    command = f"{door_id}:{action}"
    ser.write(command.encode())
    ser.close()

def check_access(card_id, door_id, action):
    try:
        person = Person.objects.get(card_id=card_id)
        door = Door.objects.get(door_id=door_id)
        access_granted = person.role in ['admin', 'authorized']
        log = AccessLog.objects.create(person=person, door=door, access_granted=access_granted, action=action)
        
        # Enviar mensaje a WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "access_logs",
            {
                "type": "access_log_message",
                "message": {
                    "person": person.name,
                    "door": door.door_name,
                    "timestamp": log.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    "action": action,
                    "access_granted": access_granted
                }
            }
        )

        if access_granted:
            control_door(door_id, 'open' if action == 'entry' else 'close')
        return access_granted
    except Person.DoesNotExist:
        return False
    except Door.DoesNotExist:
        return False