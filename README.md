A ZeroMQ-based service for interacting with GPIO pins. This service runs in the background on a Raspberry Pi and is the foundation for a GPIO API Server and GPIO Socket Server.

TODO: Add links to GPIO API Server and GPIO Socket Server


## Running Tests

Tests, with code coverage reporting can be ran with the following command, on a Raspberry Pi only:
```
nosetests -v --with-coverage --cover-erase --cover-package=pi_gpio_core --cover-xml --cover-html
```


## Using the server
```python
from pi_gpio_core.server import GpioCore


GpioCore(port=5555).run()
```


## Using the client

With the server running on the Raspberry Pi

```
from pi_gpio_core.client import GpioCoreClient


client = GpioCoreClient()

# Add a digital input for pin
client.add_input(pin=13, pull_up=False, bounce_time=None)

# Add a digital output for pin
client.add_output(pin=13, active_high=True, initial_value=False)

# Turn on digital output pin
client.pin_on(pin=13)

# Turn off digital output pin
client.pin_off(pin=13)

# Read digital input or output for pin
client.pin_read(pin=13)
```
