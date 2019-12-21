from scapy.all import *
from port_scanning import config


def main():
    print(config.OPENING_MESSAGE % config.HOST)
    port = config.MIN_PORT
    while port <= config.MAX_PORT:
        my_packet = IP(dst=config.HOST) / TCP(sport=config.SOURCE_PORT, dport=port)
        response_packet = sr1(my_packet, timeout=config.PACKET_TIMEOUT, verbose=config.PACKET_VERBOSE)
        if response_packet is None:
            sys.stdout.write(config.RED)
            print(config.CLOSE_PORT_MESSAGE % port)
        else:
            sys.stdout.write(config.GREEN)
            print(config.OPEN_PORT_MESSAGE % port)
        port += 1


if __name__ == '__main__':
    main()
