from pi_gpio_core.server import Server


def main():
    Server(addr='tcp://127.0.0.1:5555').run()


if __name__ == '__main__':
    main()
