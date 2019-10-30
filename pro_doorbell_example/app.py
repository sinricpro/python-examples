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


callbacks = {}

eventsCallbacks = {
    'Events': Events
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceId, callbacks, event_callbacks=event_callback, enable_trace=False,
                       enable_track=True, secretKey=secretKey)
    udp_client = SinricProUdp(callbacks, enable_trace=False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)