# simple_mop

Simple example to automate MOP show commands


## Business/Technical Challenge

Speed up the execution of show command across different devices

## Proposed Solution


This script provides an example, mainly for learning purposes, on how
simple (very simple) MOP automation can be done. For complex MOPs, refer to
[Cisco Network Services Orchestrator](https://www.cisco.com/c/en/us/solutions/service-provider/solutions-cloud-providers/network-services-orchestrator-solutions.html)


### Cisco Products Technologies/ Services

Cisco XR

Our solution will levegerage the following Cisco technologies

* [Cisco XR](https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xr-software/products-release-notes-list.html)
* [Cisco NX](https://www.cisco.com/c/en/us/products/ios-nx-os-software/nx-os/index.html)
* [Cisco XE](https://www.cisco.com/c/en/us/products/ios-nx-os-software/ios-xe/index.html)

## Team Members


* sfloresk@cisco.com


## Solution Components


* [Netmiko](https://github.com/ktbyers/netmiko)

## Usage

In order to use this script you need to add your device IP, username and device type (these can be found here: https://github.com/ktbyers/netmiko) in the
mop_example.py file. For example, if targeting a NX device at 1.1.1.1 with user admin, you will replece this:

```python
# Device and show commands parameters
deviceIp = ""
deviceType = ""
username = ""
```

For this:
```python
# Device and show commands parameters
deviceIp = "1.1.1.1"
deviceType = "cisco_nxos"
username = "admin"
```

Then, add your show commands in the show_commands.txt and execute the script:

```bash
python mop_example.py
```

The script will print the results in the console and print it into a file that ends in "results.txt"

## Installation

The only dependency is paramiko. Works for python2 and python3
```bash
pip install netmiko
```


## License

Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE.md)

## Code of Conduct

Our code of conduct is available [here](./CODE_OF_CONDUCT.md)

## Contributing

See our contributing guidelines [here](./CONTRIBUTING.md)
