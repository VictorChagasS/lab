#!/bin/bash

# Endereço IP e portas dos serviços de nome e web
NAMESERVICE_IP="192.168.1.100"
NAMESERVICE_PORT=53
WEBSERVICE_IP="192.168.1.101"
WEBSERVICE_PORT=80

# Função para imprimir informações sobre os serviços
print_service_info() {
    echo "Serviço de Nome: $NAMESERVICE_IP:$NAMESERVICE_PORT"
    echo "Serviço Web: $WEBSERVICE_IP:$WEBSERVICE_PORT"
}

# Função para iniciar a captura de tráfego
start_traffic_capture() {
    echo "Iniciando captura de tráfego..."
    sudo tcpdump -i any -w traffic_capture_$USER.pcap &
    CAPTURE_PID=$!
}

# Função para testar a conectividade com o host
test_host_connectivity() {
    ping -c 1 $NAMESERVICE_IP > /dev/null
    if [ $? -eq 0 ]; then
        echo "O host está online."
    else
        echo "O host está offline."
    fi
}

# Função para testar se os serviços estão respondendo corretamente
test_service_response() {
    echo "Testando serviço de Nome..."
    nc -zv $NAMESERVICE_IP $NAMESERVICE_PORT
    echo "Testando serviço Web..."
    nc -zv $WEBSERVICE_IP $WEBSERVICE_PORT
}

# Função para encerrar a captura de tráfego
stop_traffic_capture() {
    echo "Encerrando captura de tráfego..."
    sudo kill -SIGINT $CAPTURE_PID
}

# Função principal
main() {
    print_service_info
    start_traffic_capture
    test_host_connectivity
    test_service_response
    stop_traffic_capture
}

# Chamada da função principal
main
