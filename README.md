A ZeroMQ-based service for interacting with GPIO pins. This service runs in the background on a Raspberry Pi and is the foundation for a GPIO API Server and GPIO Socket Server.

TODO: Add links to GPIO API Server and GPIO Socket Server


## Install it

This project is Python 3 only. If Python 3 is not your default Python, use `pip3` instead of `pip`:
```
sudo pip install pi_gpio_core
```


## Start a server

```python
from pi_gpio_core.server import gpio_core_server


server = gpio_core_server(rpc_port=5555, pub_port=5556)
server.run()
```


## Using the client

With the server running on the Raspberry Pi, you can start a client from another Python process.

```python
from pi_gpio_core.client import GpioCoreClient


client = GpioCoreClient(port=5555)

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


## Running Tests

Tests, with code coverage reporting can be ran with the following command, on a Raspberry Pi only:
```
nosetests -v --with-coverage --cover-erase --cover-package=pi_gpio_core --cover-xml --cover-html
```
