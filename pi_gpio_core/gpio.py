from jsonrpc import dispatcher
import gpiozero
from .exceptions import PinError


PINS = {}


@dispatcher.add_method
def add_input(pin, pull_up=False, bounce_time=None):
    PINS[pin] = gpiozero.DigitalInputDevice(pin, pull_up=pull_up, bounce_time=bounce_time)


@dispatcher.add_method
def add_output(pin):
    pass


@dispatcher.add_method
def read(pin):
    try:
        return PINS[pin].value
    except KeyError:
        raise PinError('Pin not active')


@dispatcher.add_method
def on(pin):
    try:
        PINS[pin].on()
    except KeyError:
        raise PinError('Pin not active')
    return PINS[pin].value


@dispatcher.add_method
def off(pin):
    try:
        PINS[pin].off()
    except KeyError:
        raise PinError('Pin not active')
    return PINS[pin].value
