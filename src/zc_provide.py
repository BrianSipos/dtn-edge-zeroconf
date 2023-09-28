#!/usr/bin/env python3

import argparse
import socket
import sys
import time
import ifaddr
from zeroconf import (
    Zeroconf,
    ServiceInfo,
)


SVCLOCAL = '_dtn-bundle._tcp.local.'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface')
    parser.add_argument('--hostname')
    parser.add_argument('--instance')
    args = parser.parse_args()
    
    zco = Zeroconf()
    
    instlocal = (args.instance + '.' if args.instance else '') + SVCLOCAL
    hostname = args.hostname or socket.gethostname().split('.', 1)[0]
    if args.interface:
        hostaddr = []
        for adapter in ifaddr.get_adapters():
            if adapter.nice_name == args.interface:
                for ipobj in adapter.ips:
                    if isinstance(ipobj.ip, tuple):
                        addr = ipobj.ip[0]
                    else:
                        addr = ipobj.ip
                    hostaddr.append(addr)
    else:
        hostaddr = [
            socket.gethostbyname(socket.gethostname())
        ]
    servinfo = ServiceInfo(
        SVCLOCAL,
        instlocal,
        weight=1,
        server=(hostname + '.local.'),
        addresses=hostaddr,
        port=4556,
        properties=dict(
          txtvers=1,
          protovers=4,
        ),
    )
    zco.register_service(servinfo)
    print(f'mDNS registered as {instlocal} on {hostaddr}')

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    
    zco.unregister_service(servinfo)
    zco.close()

if __name__ == '__main__':
    sys.exit(main())
