#!/usr/bin/env python3

import argparse
import socket
import sys
import time
import srvlookup
from zeroconf import (
    Zeroconf,
    ServiceBrowser,
    ServiceStateChange,
)


SVCLOCAL = '_dtn-bundle._tcp.local.'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--wait', type=float, default=3,
                        help='Seconds to wait for mDNS')
    args = parser.parse_args()

    infos = []

    def on_service_state_change(zeroconf, service_type, name, state_change):
        print(f'mDNS service {name} of type {service_type} state changed: {state_change}')
        if state_change == ServiceStateChange.Added:
            info = zeroconf.get_service_info(service_type, name)
            infos.append(info)

    zco = Zeroconf()
    browser = ServiceBrowser(zco, [SVCLOCAL], handlers=[on_service_state_change])
    try:
        # Wait a fixed amount of time
        time.sleep(args.wait)
    except KeyboardInterrupt:
        pass
    zco.close()

    if infos:
        print(f'Got mDNS infos {infos}')
        return 0

    # Unicast DNS
    try:
        servinfo = srvlookup.lookup('dtn-bundle', 'tcp')
    except srvlookup.main.SRVQueryFailure as err:
        servinfo = err
    print('Got DNS result:', servinfo)
    return 1 if isinstance(servinfo, Exception) else 0

if __name__ == '__main__':
    sys.exit(main())
