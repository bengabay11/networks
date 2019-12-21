from scapy.all import *

HOSTS_UP = []
PACKET_VERBOSE = 0
PACKET_TYPE = "echo-request"


def host_is_up(host, timeout, retry):
    my_packet = IP(dst=host) / ICMP(type=PACKET_TYPE)
    response_packet = sr1(my_packet, timeout=timeout, verbose=PACKET_VERBOSE, retry=retry)
    return True if response_packet else False


def find_host(host, timeout, retry):
    if host_is_up(host, timeout, retry):
        HOSTS_UP.append(host)


def get_hosts_in_segment(segment, timeout=5, retry=3):
    list_bytes = segment.split(".")[:3]
    host = ".".join(list_bytes)
    threads_list = []
    for i in range(1, 256):
        current_host = host + "." + str(i)
        t1 = Thread(target=host_is_up, args=(current_host, timeout, retry))
        t1.start()
        threads_list.append(t1)
    for t in threads_list:
        t.join()
    return HOSTS_UP
