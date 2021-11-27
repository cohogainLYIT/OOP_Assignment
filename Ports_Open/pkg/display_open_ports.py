"""
#
#   File        :   display_open_ports.py
#   Created     :   27/11/2021 16:31
#   Author      :   Ciarán Ó hÓgáin
#   Version     :   v1.0
#   Description :   Scan and display what network ports are open on hosted virtual machine.
#
"""

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    subprocess.call("cls", shell=True)

    remoteServer = "192.168.0.59"
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    t1 = datetime.now()

    common_ports_dict = {"Secure Shell (SSH)": 22, "Simple Mail Transfer Protocol (SMTP)": 25,
                         "Domain Name System (DNS)": 53, "Hypertext Transfer Protocol (HTTP)": 80,
                         "Network Time Protocol (NTP)": 123, "Border Gateway Protocol (BGP)": 179,
                         "HTTP Secure (HTTPS)": 443}
    common_ports_val_list = list(common_ports_dict.values())
    common_ports_key_list = list(common_ports_dict.keys())

    try:
        for i in range(0, len(common_ports_val_list)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, common_ports_val_list[i]))
            if result == 0:
                print("Port " + str(common_ports_val_list[i]) +
                      "\t\t" + common_ports_key_list[common_ports_val_list.index(common_ports_val_list[i])])

            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()

    total = t2 - t1

    print("\nScanning Completed in: ", total)


if __name__ == "__main__":
    port_scan()
