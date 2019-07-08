from sinric import SinricPro
from sinric import SinricProUdp
from credentials import apiKey, deviceId

tempStates = {
    'powerLevel': 0,
}


def power_state(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state['state'])
    return True, state['state']


def set_power_level(did, state):
    # Alexa, set power level of device to 50%
    print(did, 'PowerLevel : ', state)
    tempStates['powerLevel'] = state

    return True, tempStates['powerLevel']


def adjust_power_level(did, state):
    # Alexa increase/decrease power level by 30
    print(did, 'PowerLevelDelta : ', state)

    tempStates['powerLevel'] += state
    print(tempStates['powerLevel'])

    if tempStates['powerLevel'] > 100:
        tempStates['powerLevel'] = 100
    elif tempStates['powerLevel'] < 0:
        tempStates['powerLevel'] = 0

    return True, tempStates['powerLevel']


callbacks = {
    'powerState': power_state,
    'setPowerLevel': set_power_level,
    'adjustPowerLevel': adjust_power_level
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks)
    client.socket.enableRequestPrint(False)  # Set it to True to start printing request JSON
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
