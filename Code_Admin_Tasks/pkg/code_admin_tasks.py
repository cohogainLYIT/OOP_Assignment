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

global username
global password

username = "******"
password = "******"


# Open ssh connection to the device
def open_ssh_connection(ip):
    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n)"), username=username, password=password)

        return session

    except paramiko.AuthenticationException:
        print("Authentication Error")


# Close ssh connection the device
def close_ssh_connection(connection):
    print("Closing connection...")
    time.sleep(1)
    connection.close()


# send sudo apt-get update command to VM
def apt_update(connection):
    print("\nUpdating...")
    stdin, stdout, stderr = connection.exec_command("echo " + password + "| sudo -S apt update")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


# send install curl command to VM
def install_curl(connection):
    print("\nInstalling Curl...")
    stdin, stdout, stderr = connection.exec_command("echo " + password + "| sudo -S apt install curl")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


# create parent folder Labs with two child folders Lab1 and Lab2 within
def mkdir_labs(connection):
    print("\nCreating directories...")
    stdin, stdout, stderr = connection.exec_command("mkdir Labs \n cd Labs \n mkdir Lab1 \n mkdir Lab2")
    stdin.write(password)


# find when files in VM directory were last accessed
def last_accessed(connection):
    print("\nFinding last accessed time...")
    stdin, stdout, stderr = connection.exec_command("ls -l --time=atime")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


if __name__ == "__main__":
    session = open_ssh_connection("192.168.0.59")
    apt_update(session)
    install_curl(session)
    mkdir_labs(session)
    last_accessed(session)
    close_ssh_connection(session)
