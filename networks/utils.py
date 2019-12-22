from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

PACKET_TYPE = "echo-request"
PACKET_VERBOSE = 0


def host_is_up(host, timeout, ttl=30, retry=1):
    my_packet = IP(dst=host, ttl=ttl) / ICMP(type=PACKET_TYPE)
    response_packet = sr1(my_packet, timeout=timeout, verbose=PACKET_VERBOSE, retry=retry)
    return True if response_packet else False


def wait_for_threads(threads):
    for thread in threads:
        thread.join()
