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


# Open ssh connection to the device
def ssh_connection(ip):
    try:
        username = "cohogain"
        password = "Oberc1999?"

        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n)"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send("echo 'Connection successful' > connection_success.txt\n")
        time.sleep(1)

        vm_output = connection.recv(65535)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Command successfully executed on {}".format(ip))

        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


ssh_connection("192.168.0.59")
