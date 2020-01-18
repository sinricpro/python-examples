from sinric import SinricPro
from sinric import SinricProUdp
from credentials import appKey, switchId, secretKey, deviceIdArr
from time import sleep


def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE

        # client.event_handler.raiseEvent(tvId, 'setPowerState',data={'state': 'On'})
        sleep(2)


event_callback = {
    'Events': Events
}

callbacks = {
    'powerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,
        event_callbacks=event_callback, enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)