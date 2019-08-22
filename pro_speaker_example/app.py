from sinric import SinricPro
from sinric import SinricProUdp
from credentials import apiKey, deviceId, speakerId
from time import sleep


def Events():
    while True:
        # Select as per your requirements
        # REMOVE THE COMMENTS TO USE

        # client.event_handler.raiseEvent(speakerId, 'setBands',data={'name': '','level': 0})
        # client.event_handler.raiseEvent(speakerId, 'setMode',data={'mode': ''})
        sleep(2)


event_callback = {
    'Events': Events
}


def onPowerState(deviceId, state):
    # Do Something
    return True, state


def onSetBands(deviceId, name,level):
    print(name,level)

    # Do Somethign
    return True, {'name': name,'level': level}


def onAdjustBands(deviceId, name,level,direction):
    # Do something with level

    return True, {'name': name,'level': level}


def onResetBands(deviceId, band1,band2,band3):
    # Do something with reset
    return True


def onSetMode(deviceId, mode):
    # Do something with mode
    return True, mode


callbacks = {
    'powerState': onPowerState,
    'setBands': onSetBands,
    'setMode': onSetMode,
    'adjustBands': onAdjustBands,
    'resetBands': onResetBands
}

if __name__ == '__main__':
    client = SinricPro(apiKey, deviceId, callbacks, event_callback, enable_trace=True, enable_track=True) 
    udp_client = SinricProUdp(callbacks)
    udp_client.enableUdpPrint(False)  # Set it to True to start printing request UDP JSON
    client.handle_all(udp_client)
