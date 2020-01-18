from sinric import SinricPro
from credentials import appKey, deviceId, secretKey, speakerId, deviceIdArr
from sinric import SinricProUdp



def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE

        # client.event_handler.raiseEvent(speakerId, 'setBands',data={'name': '','level': 0})
        # client.event_handler.raiseEvent(speakerId, 'setMode',data={'mode': ''})
        # client.event_handler.raiseEvent(speakerId, 'setLockState',data={'mute': True})
        pass


event_callback = {
    'Events': Events
}


def onPowerState(deviceId, state):
    # Do Something
    return True, state


def onSetBands(deviceId, name, level):
    print(name, level)

    # Do Somethign
    return True, {'name': name, 'level': level}


def onAdjustBands(deviceId, name, level, direction):
    # Do something with level

    return True, {'name': name, 'level': level}


def onResetBands(deviceId, band1, band2, band3):
    # Do something with reset
    return True


def onSetMode(deviceId, mode):
    # Do something with mode
    return True, mode


def onSetMute(deviceId, mute):
    # Muted : True, Not muted : False
    return True, mute


callbacks = {
    'powerState': onPowerState,
    'setBands': onSetBands,
    'setMode': onSetMode,
    'adjustBands': onAdjustBands,
    'resetBands': onResetBands,
    'setMute': onSetMute
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,
        event_callbacks=event_callback, enable_log=False,restore_states=True,secretKey=secretKey)
    udp_client = SinricProUdp(callbacks,deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
    client.handle_all(udp_client)
