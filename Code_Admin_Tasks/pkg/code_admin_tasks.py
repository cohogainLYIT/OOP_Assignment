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


# Open ssh connection to the host device using paramiko
def open_ssh_connection(ip):
    """
    :param: ip: ip address to host machine

    :return: session: paramiko ssh connection to host machine
    """
    try:
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n)"), username=input("Enter username"), password=input("Enter password"))
        print("Connected...")

        return session

    except paramiko.AuthenticationException:
        print("Authentication Error")


# Close ssh connection to the host device
def close_ssh_connection(connection):
    """
    :param: connection: paramiko ssh connection to host machine

    :return:
    """
    print("Closing connection...")
    time.sleep(1)
    connection.close()


# send sudo apt-get update command to host VM
def apt_update(connection):
    """
    :param: connection: paramiko ssh connection to host machine

    :return:
    """
    print("\nUpdating...")
    stdin, stdout, stderr = connection.exec_command("echo " + password + "| sudo -S apt update")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


# send install curl command to host VM
def install_curl(connection):
    """
    :param: connection: paramiko ssh connection to host machine

    :return:
    """
    print("\nInstalling Curl...")
    stdin, stdout, stderr = connection.exec_command("echo " + password + "| sudo -S apt install curl")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


# create parent folder Labs with two child folders Lab1 and Lab2 within
def mkdir_labs(connection):
    """
    :param: connection: paramiko ssh connection to host machine

    :return:
    """
    print("\nCreating directories...")
    stdin, stdout, stderr = connection.exec_command("mkdir Labs \n cd Labs \n mkdir Lab1 \n mkdir Lab2")
    stdin.write(password)


# find when files in host VM's directory were last accessed
def last_accessed(connection):
    """
    :param: connection: paramiko ssh connection to host machine

    :return:
    """
    print("\nFinding last accessed time...")
    stdin, stdout, stderr = connection.exec_command("ls -l --time=atime")
    stdin.flush()
    print(stdout.readlines())
    time.sleep(1)


# call functions to connect to host device, send update, install curl,
# make directories, view when files were last accessed and close connection again
if __name__ == "__main__":
    session = open_ssh_connection("192.168.0.59")
    apt_update(session)
    install_curl(session)
    mkdir_labs(session)
    last_accessed(session)
    close_ssh_connection(session)
