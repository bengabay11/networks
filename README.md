<a name="network-scripts"></a>
# network-scripts
Useful network scripts written in python.

<a name="table-of-contents"></a>
## Table of contents
1. [network-scripts](#network-scripts)
2. [Table of contents](#table-of-contents)
3. [Installation](#installation)
4. [Scripts](#scripts)
    * [Arp Spoofing](#arp-spoofing)
    * [Traceroute](#traceroute)
    * [Port Scanning](#port-scanning)
    * [Ping](#ping)


<a name="installation"></a>
## Installation
Clone the repository and install all dependencies
```
$ pip install -r requiments.txt
```

<a name="scripts"></a>
## Scripts

<a name="arp-spoofing"></a>
### Arp Spoofing
Description will come soon.
#### Usage
```
$ cd arp_spoofing
$ python arps.py <host to attack> <host to impersonate>
```

<a name="traceroute"></a>
### Traceroute
A simple implementation of the tracert command using the scapy package.
#### Usage
```
$ cd traceroute
$ python app.py <host>
```

<a name="#port-scanning"></a>
### Port Scanning
Description will come soon.
#### Usage
```
$ cd port_scanning
$ python app.py
```

<a name="#ping"></a>
### Ping
Description will come soon.
#### Usage
```
$ cd ping
$ python app.py [-h] [-c --count] [-i --ttl] [-t --timeout] <target_host>
```
