from sinric import SinricPro
from credentials import apiKey, deviceId
from sinric import SinricProUdp


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
    client = SinricPro(apiKey, deviceId, callbacks, enable_trace=False)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
