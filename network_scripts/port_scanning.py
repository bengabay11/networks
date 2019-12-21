import datetime
import socket

PACKET_TIMEOUT = 2


def print_status_message(port, is_open):
    if is_open:
        message = f"port {port} is open."
    else:
        message = f"port {port} is close."
    print(message)


def open_is_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))
    return True if result == 0 else False


def timeout_override(start_time, timeout):
    if timeout:
        timeout = datetime.timedelta(seconds=timeout)
        current_time = datetime.datetime.now()
        return start_time + timeout <= current_time
    return False


def port_scanning(target, min_port=1, max_port=65536, timeout=None, verbose=True):
    """
    Perform port scanning on the given target.
    :param target: target to scan.
    :param min_port: (optional) the starting port. default=1
    :param max_port: (optional) the ending port. default=65536
    :param timeout: (optional) max time in seconds to perform the scan. default=None
    :param verbose: (optional) print output. default=True
    :return: Dictionary. e.g.: { "22": False, "80": True }
    """
    ports = {}
    start_time = datetime.datetime.now()
    for current_port in range(min_port, max_port):
        if timeout_override(start_time, timeout):
            break
        is_open = open_is_port(target, current_port)
        if verbose:
            print_status_message(current_port, is_open)
        ports[str(current_port)] = is_open
        current_port += 1
    return ports
