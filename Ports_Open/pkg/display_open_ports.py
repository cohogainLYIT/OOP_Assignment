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


# scan through commonly used ports and check if open. Print open port number and description
def port_scan(remoteServer):
    """
    :param: remoteServer: ip to remote server for port scanning

    :return:
    """
    subprocess.call("cls", shell=True)
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("\nScanning remote host", remoteServerIP)
    print("_"*50)

    # dictionary of commonly used network ports
    common_ports_dict = {"Secure Shell (SSH)": 22, "Simple Mail Transfer Protocol (SMTP)": 25,
                         "Domain Name System (DNS)": 53, "Hypertext Transfer Protocol (HTTP)": 80,
                         "Network Time Protocol (NTP)": 123, "Border Gateway Protocol (BGP)": 179,
                         "HTTP Secure (HTTPS)": 443}

    # key and value list of dictionary
    common_ports_val_list = list(common_ports_dict.values())
    common_ports_key_list = list(common_ports_dict.keys())

    # loop through commonly used network ports and check if they are open
    try:
        for i in range(0, len(common_ports_val_list)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, common_ports_val_list[i]))
            if result == 0:
                print("Port " + str(common_ports_val_list[i]) +
                      "\t\t" + common_ports_key_list[common_ports_val_list.index(common_ports_val_list[i])])

            sock.close()

    # catch program if user enters Ctrl+C
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    # catch program if there are connection issues
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    # catch program if there are connection issues
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()


if __name__ == "__main__":
    # run port scan on VM
    port_scan("192.168.0.59")
