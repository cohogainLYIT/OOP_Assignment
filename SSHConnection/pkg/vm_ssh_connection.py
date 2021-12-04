"""
#
#   File        :   vm_ssh_connection.py
#   Created     :   27/11/2021 15:32
#   Author      :   Ciarán Ó hÓgáin
#   Version     :   v1.0
#   Description :   Establish an SSH connection with virtual machine
#
"""

import paramiko
import time
import re


# Open ssh connection to host device and display if connection successful
def ssh_connection(ip):
    """
    :param: ip: ip address of host device

    :return: none
    """
    try:
        # connect to host VM using paramiko package
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n)"), username=input("Enter username:\t\t"), password=input("Enter password:\t\t"))
        print("Connection Successful.")
        connection = session.invoke_shell()
        connection.send("echo 'Connection successful' > connection_success.txt\n")
        time.sleep(1)

        session.close()

    # catch authentication error
    except paramiko.AuthenticationException:
        print("Authentication Error.")


if __name__ == '__main__':
    # connect to VM IP address using by calling ssh_connection function
    ssh_connection("192.168.0.59")
