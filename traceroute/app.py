from scapy.all import *
import config
import validator


def send_packet(address, ttl_index):
    my_packet = IP(dst=address, ttl=ttl_index) / ICMP(type=config.PACKET_TYPE)
    response_packet = sr1(my_packet, timeout=config.PACKET_TIMEOUT, verbose=config.PACKET_VERBOSE)

    return response_packet


def trace(address):
    ttl_index = 1
    current_hop = 1
    print(config.MAX_HOPS_MESSAGE + str(config.MAX_HOPS))
    while True:
        start_time = time.time()
        response_packet = send_packet(address, ttl_index)
        final_time = (time.time() - start_time) / 60 * 1000
        if response_packet is not None:
            print("{index})  {time} ms {packet_src}".format(
                index=str(current_hop), time=str(int(final_time)), packet_src=response_packet[IP].src))
            if response_packet[ICMP].type != config.TTL_EXCEED:
                break
        else:
            print((str(current_hop) + ")  " + config.REQUEST_TIME_OUT_MESSAGE))

        ttl_index += 1
        current_hop += 1


def main():
    if len(sys.argv) == 2:
        address = sys.argv[1]
        if validator.validate_ip(address) or validator.validate_url(address):
            print("{newline}{trace_message}{address}"
                  .format(newline=os.linesep, trace_message=config.TRACE_MESSAGE, address=address))
            trace(address)
        else:
            sys.exit(config.INVALID_ADDRESS_MESSAGE)
    else:
        print(config.INVALID_ARGUMENTS_MESSAGE)


if __name__ == '__main__':
    main()
