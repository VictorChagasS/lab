#!/usr/bin/python

import os
import subprocess
import socket

NAMESERVICE_IP = "192.0.2.100"
NAMESERVICE_PORT = 53
WEBSERVICE_IP = "192.168.1.101"
WEBSERVICE_PORT = 80

def print_service_info():
    print("Servico de Nome:", NAMESERVICE_IP + ":" + str(NAMESERVICE_PORT))
    print("Servico Web:", WEBSERVICE_IP + ":" + str(WEBSERVICE_PORT))

def start_traffic_capture():
    print("Iniciando captura de trafego...")
    os.system("sudo tcpdump -i any -w traffic_capture_VictorChagas.pcap &")

def test_host_connectivity():
    response = os.system("ping -c 1 " + NAMESERVICE_IP)
    if response == 0:
        print("O host esta online.")
    else:
        print("O host esta offline.")

def test_service_response():
    print("Testando servico de Nome...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = s.connect_ex((NAMESERVICE_IP, NAMESERVICE_PORT))
        if result == 0:
            print("Servico de Nome esta respondendo corretamente.")
        else:
            print("Nao foi possivel conectar ao servico de Nome.")
    finally:
        s.close()

    print("Testando servico Web...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = s.connect_ex((WEBSERVICE_IP, WEBSERVICE_PORT))
        if result == 0:
            print("Servico Web esta respondendo corretamente.")
        else:
            print("Nao foi possivel conectar ao servico Web.")
    finally:
        s.close()

def stop_traffic_capture():
    print("Encerrando captura de trafego...")
    os.system("sudo pkill tcpdump")

def main():
    print_service_info()
    start_traffic_capture()
    test_host_connectivity()
    test_service_response()
    stop_traffic_capture()

if __name__ == "__main__":
    main()
