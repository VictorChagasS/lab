#!/usr/bin/python
import socket

def handle_request(client_socket):
    http_response = """\
HTTP/1.1 200 OK

<html>
<head>
<title>Empresa A: Acessibilidade em Foco</title>
</head>
<body>
<h1>Bem-vindo à Empresa A: Acessibilidade em Foco</h1>
<p>Nossa missão é promover a inclusão e a igualdade de acesso ao conhecimento para todas as pessoas, especialmente para a comunidade surda. Oferecemos uma plataforma inovadora de ensino da Língua Brasileira de Sinais (Libras), integrada ao Canvas, para capacitar indivíduos a se comunicarem efetivamente.</p>
<h2>O que Oferecemos:</h2>
<ul>
<li>Plataforma de Ensino de Libras: Acesso a uma experiência de aprendizado interativa e acessível.</li>
<li>Recursos Multimídia: Vídeos, exercícios práticos e quizzes para facilitar a compreensão e a prática da Libras.</li>
<li>Suporte Personalizado: Equipe de instrutores qualificados disponível para oferecer suporte personalizado aos alunos.</li>
</ul>
<h2>Por que Escolher a Empresa A:</h2>
<p>Escolha a Empresa A e junte-se a nós na jornada rumo a um mundo mais inclusivo e acessível, onde a comunicação não conheça barreiras.</p>
</body>
</html>
"""
    client_socket.sendall(http_response.encode())
    client_socket.close()  # Fechar explicitamente o socket do cliente após enviar a resposta

def run_server(host='', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Servidor rodando em http://{host}:{port}')
    while True:
        client_socket, _ = server_socket.accept()
        handle_request(client_socket)
        client_socket.close()  # Fechar explicitamente o socket do cliente após tratamento

if __name__ == "__main__":
    run_server()
