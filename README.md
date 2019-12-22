<a name="networks"></a>
# networks
Python Network Operations for Humans

<a name="table-of-contents"></a>
## Table of contents
1. [networks](#networks)
2. [Table of contents](#table-of-contents)
4. [Examples](#examples)
    * [Traceroute](#traceroute)
    * [Arp Spoofing](#arp-spoofing)
    * [Port Scanning](#port-scanning)
    * [Ping](#ping)

<a name="examples"></a>
## Examples

<a name="traceroute"></a>
### Traceroute
Perform trace to the given host.
```pycon
>>> import networks
>>> stations = networks.trace("www.google.com", max_hops=20, timeout=5)
>>> stations
['192.168.1.1', '0.0.0.0', None, '172.18.9.214', '172.17.3.118', None, None, '209.85.241.75', '172.217.18.100']
```

<a name="arp-spoofing"></a>
### Arp Spoofing
Perform arp spoofing attack on the given target.
```pycon
>>> import networks
>>> target = "192.168.1.40"
>>> gateway = "192.168.1.1"
>>> networks.arp_spoofing(target, gateway, interval=1, timeout=120)
```


<a name="#port-scanning"></a>
### Port Scanning
Perform port scanning on the given target.
```pycon
>>> import networks
>>> ports = networks.port_scanning("192.168.1.40", min_port=78, max_port=81, timeout=30)
>>> ports
{78: False, 79: False, 80: True, 81: False, 82: False}
```

<a name="#ping"></a>
### Ping
Send ICMP packets to the given host.
```pycon
>>> import networks
>>> host_responded = networks.ping("www.google.com", count=5, ttl=30, timeout=5)
>>> host_responded
True
```

<a name="#ping"></a>
### Hosts in segment
get hosts inside a given segment.
```pycon
>>> import networks
>>> hosts = networks.get_hosts_in_segment("192.168.1.0")
>>> hosts
['192.168.1.1', '192.168.1.40', '192.168.1.23']
```
