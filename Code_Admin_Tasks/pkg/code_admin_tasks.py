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

username = "cohogain"
password = "Oberc1999?"


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


def close_ssh_connection(connection):
    print("Closing connection...")
    time.sleep(1)
    connection.close()


def apt_update(connection):
    print("\nUpdating...")
    stdin, stdout, stderr = connection.exec_command("echo " + password + "| sudo -S apt update")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


def install_curl(connection):
    print("\nInstalling Curl...")
    stdin, stdout, stderr = connection.exec_command("echo " + password + "| sudo -S apt install curl")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


def mkdir_labs(connection):
    print("\nCreating directories...")
    stdin, stdout, stderr = connection.exec_command("mkdir Labs \n cd Labs \n mkdir Lab1 \n mkdir Lab2")
    stdin.write(password)


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
