from pi_gpio_core.server import Server


def main():
    Server(addr='tcp://*:5555').run()


if __name__ == '__main__':
    main()
