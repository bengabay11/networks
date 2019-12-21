<a name="networks"></a>
# networks
python package for useful network scripts

<a name="table-of-contents"></a>
## Table of contents
1. [network-scripts](#networks)
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
```
>>> import networks
>>> stations = networks.trace("www.google.com", max_hops=20, timeout=5, verbose=False)
>>> for station in stations:
>>>     print(station)
```

<a name="arp-spoofing"></a>
### Arp Spoofing
Perform arp spoofing attack on the given target.
```
>>> import networks
>>> target = "192.168.1.40"
>>> gateway = "192.168.1.1"
>>> networks.arp_spoofing(target, gateway, interval=1, timeout=120)
```


<a name="#port-scanning"></a>
### Port Scanning
Perform port scanning on the given target.
```
>>> import networks
>>> ports = networks.port_scanning("192.168.1.40", min_port=1, max_port=100, timeout=30)
>>> for (port_number, is_open) in ports:
>>>     if is_open:
>>>         print("Discoverd open port: {port}")
```

<a name="#ping"></a>
### Ping
Send ICMP packets to the given host.
```
>>> import networks
>>> host_responded = networks.ping("www.google.com", count=5, ttl=30, timeout=5)
>>> if host_responded:
>>> print("host: {host} is up!")
```

```
>>> segment = "192.168.1.0"
>>> hosts = networksget_hosts_in_segment(segment, timeout=5, retry=3)
>>> print(f"{len(hosts)} hosts found.")
>>> for host in hosts:
>>> print(f"- {host}")
```
