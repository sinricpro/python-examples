from sinric import SinricPro
from sinric import SinricProUdp
from credentials import appKey, garageId, secretKey, deviceIdArr
from time import sleep



def onPowerState(did, state):
    print(did, state)
    return True, did
def onGarageAction(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state

callbacks = {
    'setMode': onGarageAction,
    'onPowerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,
         enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)