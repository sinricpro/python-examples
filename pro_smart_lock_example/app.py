from sinric import SinricPro
from sinric import SinricProUdp
from credentials import apiKey, lockId, deviceId
from time import sleep


def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE

        # client.event_handler.raiseEvent(lockId, 'setLockState',data={'state': 'LOCKED'})
        # client.event_handler.raiseEvent(lockId, 'setLockState',data={'state': 'UNLOCKED'})
        sleep(2)


event_callback = {
    'Events': Events
}


def onSetLockState(deviceId, state):
    return True, state


callbacks = {
    'setLockState': onSetLockState
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks, event_callback, enable_trace=True)
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
