from pi_gpio_core.server import GpioCore


def main():
    GpioCore(port=5555).run()


if __name__ == '__main__':
    main()
