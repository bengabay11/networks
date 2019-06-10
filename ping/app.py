import argparse
from _socket import gaierror
from scapy.all import *
import time
import config


def ping(destination_address, count, ttl, timeout):
    print(config.OPENING_MESSAGE.format(destination_address))
    try:
        my_packet = IP(dst=destination_address, ttl=ttl) / ICMP(type=config.PACKET_TYPE)
        for i in range(count):
            start_time = time.time()
            response_packet = sr1(my_packet, timeout=timeout, verbose=config.PACKET_VERBOSE)
            end_time = time.time()
            response_time = int(end_time-start_time)
            if response_packet:
                print(config.REPLY_MESSAGE.format(destination_address, response_time, ttl))
            else:
                print(config.TIMED_OUT_MESSAFE)
    except gaierror:
        print("Illegal IP address or host given.")


def main():
    parser = argparse.ArgumentParser(description='Check the connectivity to the requested host.')
    parser.add_argument('-c', metavar='--count', type=int, default=config.DEFAULT_COUNT,
                        help='the number of the packets to send to the host.')
    parser.add_argument('-i', metavar='--ttl', type=int, default=config.DEFAULT_TTL, help="time to live.")
    parser.add_argument('-t', metavar='--timeout', type=int, default=config.DEFAULT_TIMEOUT,
                        help="the time in seconds till the the packet will stop waiting for answer.")
    parser.add_argument('target_host', type=str)

    args = parser.parse_args()
    ping(args.target_host, args.c, args.i, args.t)


if __name__ == '__main__':
    main()
