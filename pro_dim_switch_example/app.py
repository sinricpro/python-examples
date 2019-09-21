from sinric import SinricPro
from sinric import SinricProUdp
from credentials import appKey, deviceId, secretKey,deviceId1
from time import sleep

def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE
        # client.event_handler.raiseEvent(deviceId1, 'setPowerState',data={'state': 'On'})
        sleep(2)


def onPowerState(deviceId, state):
    # Alexa, turn ON/OFF Device
    print(deviceId, state)
    return True, state


def onSetPowerLevel(deviceId, state):
    # Alexa, set power level of device to 50%
    print(deviceId, 'PowerLevel : ', state)
    return True, state


def onAdjustPowerLevel(deviceId, state):
    # Alexa increase/decrease power level by 30
    print(deviceId, 'PowerLevelDelta : ', state)
    return True, state

eventsCallbacks={
    "Events": Events
}
callbacks = {
    'powerState': onPowerState,
    'setPowerLevel': onSetPowerLevel,
    'adjustPowerLevel': onAdjustPowerLevel
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceId, callbacks,event_callbacks=eventsCallbacks, enable_trace=False, enable_track=True, secretKey=secretKey)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
