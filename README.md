# pi-gpio-core
A ZeroMQ-based service for interacting with GPIO pins


## Running Tests

Tests, with code coverage reporting can be ran with the following command:
```
docker-compose run gpio_core_tests nosetests -v --with-coverage --cover-erase --cover-package=pi_gpio_core --cover-xml --cover-html
```
