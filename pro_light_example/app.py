from sinric import SinricPro
from credentials import appKey, lightId, secretKey, deviceIdArr
from sinric import SinricProUdp

def Events():
    while True:
    #    client.event_handler.raiseEvent(lightId, 'setPowerState',data={'state': 'On'})
    # client.event_handler.raiseEvent(deviceId1, 'setColor',data={'r': 0,'g': 0,'b': 0})
    # client.event_handler.raiseEvent(deviceId1, 'setColorTemperature',data={'colorTemperature': 2400})
        pass

eventCallbacks = {
    'Events': Events
}


def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


def onSetBrightness(did, state):
    # Alexa set device brightness to 40%
    print(did, 'BrightnessLevel : ', state)
    return True, state


def onAdjustBrightness(did, state):
    # Alexa increase/decrease device brightness by 44
    print(did, 'AdjustBrightnessLevel : ', state)

    return True, state


def onSetColor(did, r, g, b):
    # Alexa set device color to Red/Green
    print(did, 'Red: ', r, 'Green: ', g, 'Blue : ', b)

    return True


def onSetColorTemperature(did, value):
    print(did, value)
    return True


def onIncreaseColorTemperature(deviceId, value):
    return True, value


def onDecreaseColorTemperature(deviceId, value):
    return True, value


callbacks = {
    'powerState': onPowerState,
    'setBrightness': onSetBrightness,
    'adjustBrightness': onAdjustBrightness,
    'setColor': onSetColor,
    'setColorTemperature': onSetColorTemperature,
    'increaseColorTemperature': onIncreaseColorTemperature,
    'decreaseColorTemperature': onDecreaseColorTemperature
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,event_callbacks=eventCallbacks, 
        enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)
