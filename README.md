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
>>> target = "192.168.1.40"
>>> ports = networks.port_scanning(target, min_port=1, max_port=100, timeout=30)
>>> for (port_number, is_open) in ports:
>>>     print(f"port: {port}")
>>>     print("open!") if is_open else print("close")
```

<a name="#ping"></a>
### Ping
Send ICMP packets to the given host.
```
>>> import networks
>>> host = "www.google.com"
>>> host_responded = networks.ping(host, count=5, ttl=30, timeout=5)
>>> if host_responded:
>>> print("host: {host} is up!")
```
