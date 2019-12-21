from scapy.all import *

HOSTS_UP = []
PACKET_VERBOSE = 0


def host_is_up(host, timeout):
    my_packet = IP(dst=host) / ICMP(type=config.PACKET_TYPE)
    response_packet = sr1(my_packet, timeout=timeout, verbose=config.PACKET_VERBOSE, retry=config.RETRY)
    return True if response_packet else False


def get_hosts_in_segment(segment):
    list_bytes = segment.split(".")[:3]
    host = ".".join(list_bytes)
    threads_list = []
    for i in range(1, 256):
        current_host = host + "." + str(i)
        t1 = Thread(target=host_is_up, args=(current_host, ))
        t1.start()
        threads_list.append(t1)

    for t in threads_list:
        t.join()

    return HOSTS_UP
