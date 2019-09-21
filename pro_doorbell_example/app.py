from sinric import SinricPro
from credentials import appKey, deviceId, doorBellId,secretKey
from sinric import SinricProUdp
from sinric import eventNames
from time import sleep

'''
DON'T FORGET TO TURN ON 'Doorbell Press' IN ALEXA APP
'''


def Events():
    while True:
        client.event_handler.raiseEvent(doorBellId, eventNames['door_bell_event'])
        sleep(2)


request_callbacks = {}

event_callbacks = {
    'Events': Events
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceId, request_callbacks, event_callbacks, enable_trace=True, enable_track=True)
    udp_client = SinricProUdp(request_callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
