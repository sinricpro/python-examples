from sinric import SinricPro
from sinric import SinricProUdp
import asyncio

from credentials import appKey, customDeviceId, secretKey, deviceIdArr
 
def onPowerState(did, state):
    # Alexa, turn ON/OFF Device
    print(did, state)
    return True, state

def onRangeValue(did,rangeValue, instanceId):
    print(did, rangeValue, instanceId)
    return True, rangeValue, instanceId

def onModeValue(did, modeValue, instanceId):
    print(did, modeValue, instanceId)
    return True, modeValue, instanceId

 
callbacks = {
    'powerState': onPowerState,
    'setRangeValue': onRangeValue,
    'setMode': onModeValue
}

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    client = SinricPro(appKey, deviceIdArr, callbacks,
    enable_log=False,restore_states=True,secretKey=secretKey)

    udp_client = SinricProUdp(callbacks,deviceIdArr,
    enable_trace=False, loopInstance=loop)  # Set enable_trace to True to start logging request Offline Request/Response

    loop.run_until_complete(client.connect(udp_client=udp_client))