from sinric import SinricPro
from sinric import SinricProUdp
from credentials import apiKey, deviceId


def power_state(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state


def set_power_level(did, state):
    # Alexa, set power level of device to 50%
    print(did, 'PowerLevel : ', state)
    return True, state


def adjust_power_level(did, state):
    # Alexa increase/decrease power level by 30
    print(did, 'PowerLevelDelta : ', state)
    return True, state


callbacks = {
    'powerState': power_state,
    'setPowerLevel': set_power_level,
    'adjustPowerLevel': adjust_power_level
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks, enable_trace=False)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
