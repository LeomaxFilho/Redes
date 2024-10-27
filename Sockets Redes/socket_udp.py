'''
LUIS ALVES DE PAIVA NETO
LEOMAX DA COSTA BANDEIRA FILHO
'''


import socket
import request_response

# Especificacoes do servidor 
UDP_IP = "15.228.191.109"
UDP_PORT = 50000

# Criacao do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):   
    op = int(input("[1] Data e Hora\n[2] Mensagem Motivacional\n[3] Respostas Emitidas\n[4] Sair: "))
    
    # Gerar o identificador
    identficador = request_response.random_id()

    # * Data e hora
    if op == 1:

        # Gera a mensagem para ser enviada para o servidor
        req = request_response.gerar_requisicao(0, 0, identficador)

        # Conversao da mensagem de requisicao para um objeto de bytes
        msg = req.to_bytes(3, 'little')

        # Sock de enviando a mensagem para o servidor
        sock.sendto(msg, (UDP_IP, UDP_PORT))

        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)

        # Tipo de mensagem do servidor
        palavra = request_response.receber_resposta(int.from_bytes(msg_server, byteorder='little'))

    # * Mensagem motivacional
    elif op == 2:
        # Gera a requisicao da mensagem
        req = request_response.gerar_requisicao(0, 1, identficador)

        # Conversao da mensagem de requisicao para um objeto de bytes
        msg = req.to_bytes(3, 'little')
        
        # Sock de enviando a mensagem para o servidor
        sock.sendto(msg, (UDP_IP, UDP_PORT))

        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)
        
        palavra = request_response.receber_resposta(int.from_bytes(msg_server, byteorder='little'))


    # * Mensagem de quantidade de requisicoes
    elif op == 3:
        # Resicao da mensagem
        req = request_response.gerar_requisicao(0, 2, identficador)
        
        # Conversao da mensagem de requisicao para um objeto de bytes
        msg = req.to_bytes(3, 'little')    

        # Sock de enviando a mensagem para o servidor
        sock.sendto(msg, (UDP_IP, UDP_PORT))
        
        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)

        # Tipo de mensagem
        palavra = request_response.receber_resposta_int(int.from_bytes(msg_server, byteorder='little'))

    elif op == 4:   
        break
    else:
        print("OPCAO INVALIDA!!!")
