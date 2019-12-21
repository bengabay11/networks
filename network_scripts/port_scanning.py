from scapy.all import *
import datetime

PACKET_TIMEOUT = 2


def print_status_message(port, is_open):
    if is_open:
        message = f"port {port} is open."
    else:
        message = f"port {port} is close."
    print(message)


def open_port(target, port):
    my_packet = IP(dst=target) / TCP(sport=port, dport=port)
    response_packet = sr1(my_packet, timeout=PACKET_TIMEOUT, verbose=False)
    return bool(response_packet)


def timeout_override(start_time, timeout):
    if timeout:
        timeout = datetime.timedelta(seconds=timeout)
        current_time = datetime.datetime.now()
        return start_time + timeout <= current_time
    return False


def port_scanning(target, min_port=1, max_port=65536, timeout=None, verbose=True):
    ports = {}
    start_time = datetime.datetime.now()
    for current_port in range(min_port, max_port):
        if timeout_override(start_time, timeout):
            break
        is_open = open_port(target, current_port)
        if verbose:
            print_status_message(current_port, is_open)
        ports[str(current_port)] = {"open": is_open}
        current_port += 1
    return ports
