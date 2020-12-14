from sinric import SinricPro
from credentials import appKey, deviceIdArr, secretKey, temperatureSensorDeviceId
from sinric import SinricProUdp
from sinric import eventNames
from time import sleep

def Events():
    while True:
        client.event_handler.raiseEvent(temperatureSensorDeviceId, 'temperatureHumidityEvent', data={'humidity': 75.3, 'temperature': 24})
        sleep(60) # Server will trottle / block IPs sending events too often.
        pass

def onPowerState(did, state):
    print(did, state)
    return True, state


eventsCallbacks={
    "Events": Events
}

callbacks = {
    'powerState': onPowerState
}

if __name__ == '__main__':
    client = SinricPro(appKey, deviceIdArr, callbacks,event_callbacks=eventsCallbacks, enable_log=True,restore_states=False,secretKey=secretKey)
    client.handle_all()