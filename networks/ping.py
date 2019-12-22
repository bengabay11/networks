import time

from networks.utils import host_is_up


def ping(host, count=5, ttl=50, timeout=5, verbose=True):
    """Send ICMP packets to the given host.
    
    :param host: host to send the packets to.
    :param count: (optional) amount of packets to send. default=5
    :param ttl: (optional) Time To Live for each packet. default=50
    :param timeout: (optional) timeout in seconds. default=5
    :param verbose: (optional) print output. default=True
    :return: whether the host responded to one of the packets that sent to him.
    :rtype: bool
    """
    host_up = False
    for i in range(count):
        start_time = time.time()
        host_up = host_is_up(host, timeout, ttl)
        end_time = time.time()
        response_time = int(end_time-start_time)
        if host_up:
            message = f"Reply from {host}: time={response_time}s TTL={ttl}"
        else:
            message = "Request timed out."
        if verbose:
            print(message)
    return host_up
