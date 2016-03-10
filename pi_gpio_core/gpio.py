from jsonrpc import dispatcher
import gpiozero
from .exceptions import PinError


gpio_dispatcher = dispatcher.Dispatcher()


PINS = {}


@gpio_dispatcher.add_method
def add_input(pin, pull_up=False, bounce_time=None):
    PINS[pin] = gpiozero.DigitalInputDevice(pin, pull_up=pull_up, bounce_time=bounce_time)


@gpio_dispatcher.add_method
def add_output(pin):
    pass


@gpio_dispatcher.add_method
def read(pin):
    try:
        return PINS[pin].value
    except KeyError:
        raise PinError('Pin not active')


@gpio_dispatcher.add_method
def on(pin):
    try:
        PINS[pin].on()
    except KeyError:
        raise PinError('Pin not active')
    return PINS[pin].value


@gpio_dispatcher.add_method
def off(pin):
    try:
        PINS[pin].off()
    except KeyError:
        raise PinError('Pin not active')
    return PINS[pin].value
