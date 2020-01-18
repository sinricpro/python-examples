from sinric import SinricPro
from credentials import appKey, lockId, secretKey, deviceIdArr
from sinric import SinricProUdp

def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE

        # client.event_handler.raiseEvent(lockId, 'setLockState',data={'state': 'LOCKED'})
        # client.event_handler.raiseEvent(lockId, 'setLockState',data={'state': 'UNLOCKED'})
        pass


event_callback = {
    'Events': Events
}


def onSetLockState(deviceId, state):
    print(deviceId, state)
    return True, state


callbacks = {
    'setLockState': onSetLockState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,
        event_callbacks=event_callback, enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)
