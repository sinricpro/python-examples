from sinric import SinricPro
from sinric import SinricProUdp
from credentials import appKey, deviceId1, secretKey, deviceIdArr
from time import sleep


def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE
        # client.event_handler.raiseEvent(deviceId1, 'setPowerState',data={'state': 'On'})
        sleep(2)  # Sleep for 2 seconds


def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


eventsCallbacks = {
    "Events": Events
}

callbacks = {
    'powerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,event_callbacks=eventsCallbacks, enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)
