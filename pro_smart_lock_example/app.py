from sinric import SinricPro
from credentials import appKey, deviceId, secretKey, deviceIdArr
from sinric import SinricProUdp

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
    client = SinricPro(appKey, deviceId, callbacks, event_callbacks=event_callback, enable_trace=False,
                       enable_track=True, secretKey=secretKey)
    udp_client = SinricProUdp(callbacks, deviceIdArr,
                              enable_trace=False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
