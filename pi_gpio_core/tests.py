import unittest
from gpiozero import DigitalInputDevice
from .gpio import PINS, add_input


class GpioTestCase(unittest.TestCase):

    def setUp(self):
        super(GpioTestCase, self).setUp()

    def test_add_input(self):
        add_input(pin=10)
        self.assertIsInstance(PINS[10], DigitalInputDevice)
