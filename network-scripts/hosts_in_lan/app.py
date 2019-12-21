from scapy.all import *
import config

HOSTS_UP = []


def host_up(host):
    my_packet = IP(dst=host) / ICMP(type=config.PACKET_TYPE)
    response_packet = sr1(my_packet, timeout=config.PACKET_TIMEOUT, verbose=config.PACKET_VERBOSE, retry=config.RETRY)
    if response_packet:
        HOSTS_UP.append(host)


def get_hosts_in_lan(router):
    list_bytes = router.split(".")[:3]
    host = ".".join(list_bytes)
    list_threads = []
    for i in range(1, 256):
        current_host = host + "." + str(i)
        t1 = Thread(target=host_up, args=(current_host, ))
        t1.start()
        list_threads.append(t1)

    for t in list_threads:
        t.join()

    return HOSTS_UP


def main():
    if len(sys.argv) != 2:
        print(config.USAGE_MESSAGE)
        sys.exit(1)

    router = sys.argv[1]
    print(config.OPENING_MESSAGE.format(router))
    hosts_up = get_hosts_in_lan(router)
    print(config.HOSTS_IN_LAN_MESSAGE.format(time=datetime.now()))
    for host in hosts_up:
        print(host)


if __name__ == '__main__':
    main()
