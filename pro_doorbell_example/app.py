from sinric import SinricPro
from credentials import apiKey, deviceId, doorBellId
from sinric import SinricProUdp
from sinric import eventNames
from time import sleep
import sys

'''
DON'T FORGET TO TURN ON 'Doorbell Press' IN ALEXA APP
'''


def door_bell_event():
    # while True:
    client.event_handler.raiseEvent(doorBellId, eventNames['door_bell_event'])
    sleep(1)
    sys.exit(0)


request_callbacks = {}

event_callbacks = {
    'door_bell_event': door_bell_event
}
if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, request_callbacks, event_callbacks, enable_trace=True)
    udp_client = SinricProUdp(request_callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
