from sinric import SinricPro
from sinric import SinricProUdp
from credentials import apiKey, deviceId


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


callbacks = {
    'powerState': onPowerState,
    'setPowerLevel': onSetPowerLevel,
    'adjustPowerLevel': onAdjustPowerLevel
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks, enable_trace=False, enable_track=True)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
