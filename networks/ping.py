from scapy.all import *
import time

PACKET_VERBOSE = 0
PACKET_TYPE = "echo-request"


def send_icmp_packet(host, timeout, ttl):
    icmp_packet = IP(dst=host, ttl=ttl) / ICMP(type=PACKET_TYPE)
    return sr1(icmp_packet, timeout=timeout, verbose=PACKET_VERBOSE)


def ping(host, count=5, ttl=50, timeout=5, verbose=False):
    """Send ICMP packets to the given host.
    
    :param host: host to send the packets to.
    :param count: (optional) amount of packets to send. default=5
    :param ttl: (optional) Time To Live for each packet. default=50
    :param timeout: (optional) timeout in seconds. default=5
    :param verbose: (optional) print output. default=True
    :return: whether the host responded to one of the packets that sent to him.
    :rtype: bool
    """
    host_responded = False
    for i in range(count):
        start_time = time.time()
        response_packet = send_icmp_packet(host, timeout, ttl)
        end_time = time.time()
        response_time = int(end_time-start_time)
        if response_packet:
            host_responded = True
            message = f"Reply from {host}: time={response_time}s TTL={ttl}"
        else:
            message = "Request timed out."
        if verbose:
            print(message)
    return host_responded
