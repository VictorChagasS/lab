import os
import subprocess
import socket

# Endereço IP e portas dos serviços de nome e web
NAMESERVICE_IP = "192.168.1.100"
NAMESERVICE_PORT = 53
WEBSERVICE_IP = "192.168.1.101"
WEBSERVICE_PORT = 80

# Função para imprimir informações sobre os serviços
def print_service_info():
    print("Serviço de Nome:", NAMESERVICE_IP + ":" + str(NAMESERVICE_PORT))
    print("Serviço Web:", WEBSERVICE_IP + ":" + str(WEBSERVICE_PORT))

# Função para iniciar a captura de tráfego
def start_traffic_capture():
    print("Iniciando captura de tráfego...")
    os.system("sudo tcpdump -i any -w traffic_capture_" + os.getlogin() + ".pcap &")

# Função para testar a conectividade com o host
def test_host_connectivity():
    response = os.system("ping -c 1 " + NAMESERVICE_IP)
    if response == 0:
        print("O host está online.")
    else:
        print("O host está offline.")

# Função para testar se os serviços estão respondendo corretamente
def test_service_response():
    print("Testando serviço de Nome...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((NAMESERVICE_IP, NAMESERVICE_PORT))
        if result == 0:
            print("Serviço de Nome está respondendo corretamente.")
        else:
            print("Não foi possível conectar ao serviço de Nome.")

    print("Testando serviço Web...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex((WEBSERVICE_IP, WEBSERVICE_PORT))
        if result == 0:
            print("Serviço Web está respondendo corretamente.")
        else:
            print("Não foi possível conectar ao serviço Web.")

# Função para encerrar a captura de tráfego
def stop_traffic_capture():
    print("Encerrando captura de tráfego...")
    os.system("sudo pkill tcpdump")

# Função principal
def main():
    print_service_info()
    start_traffic_capture()
    test_host_connectivity()
    test_service_response()
    stop_traffic_capture()

# Chamada da função principal
if __name__ == "__main__":
    main()
