# pi-gpio-core
A ZeroMQ-based service for interacting with GPIO pins


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

# Add a digital input for pin 13
client.add_input(pin=13, pull_up=False, bounce_time=None)

# Read digital input for pin 13
client.pin_read(pin=13)
```
