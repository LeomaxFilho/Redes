import socket
import requisidor
import struct

# Especificacoes do servidor 
UDP_IP = "15.228.191.109"
UDP_PORT = 50000

# Criacao do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):   
    op = int(input(print("[1] Data e Hora\n[2] Mensagem Motivacional\n[3] Respostas Emitidas\n[4] Sair: ")))

    # Data e hora
    if op == 1:
        # Gera o identificador
        identficador = requisidor.random_id()
        # Gera a mensagem para ser enviada para o servidor
        req = requisidor.gerar_requisicao(0, 0, identficador)
        # Conversao da mensagem de requisicao para um objeto de bytes
        msg = req.to_bytes(3, 'little')
        # Sock de enviando a mensagem para o servidor
        sock.sendto(msg, (UDP_IP, UDP_PORT))
        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)
        # Exibindo a mensagem em bytes do servidor e o endereco
        print(f"Mensagem do Servidor: {msg_server}")
        print(f"Endereco: {addr}")
        # Mensagem em binario do servidor
        representacao_binaria = ''.join(format(byte, '08b') for byte in msg_server)
        print(representacao_binaria)    
        # Tipo de mensagem do servidor
        requisidor.receber_resposta(int.from_bytes(msg_server, byteorder='little'))


    # Mensagem motivacional
    elif op == 2:   
        # Gerar o Identificador
        identficador = requisidor.random_id()
        # Gera a requisicao da mensagem
        req = requisidor.gerar_requisicao(0, 1, identficador)

        print(bin(req))

        # Conversao da mensagem de requisicao para um objeto de bytes
        msg = req.to_bytes(3, 'little')
        
        representacao_binaria = ''.join(format(byte, '08b') for byte in msg)
        print(representacao_binaria)    
        
        # Sock de enviando a mensagem para o servidor
        sock.sendto(msg, (UDP_IP, UDP_PORT))
        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)
        # Exibindo a mensagem em bytes do servidor e o endereco
        """print(f"Mensagem do Servidor: {msg_server}")
        print(f"Endereco: {addr}")"""
        # Mensagem em binario do servidor
        representacao_binaria = ''.join(format(byte, '08b') for byte in msg_server)
        print(representacao_binaria)    
        
        requisidor.receber_resposta(int.from_bytes(msg_server, byteorder='little'))


    # Mensagem de quantidade de requisicoes
    elif op == 3:  
        # Gerar o identificador
        identficador = requisidor.random_id()
        # Resicao da mensagem
        
        req = requisidor.gerar_requisicao(0, 2, identficador)
        # Conversao da mensagem de requisicao para um objeto de bytes
        print(bin(req))
        msg = req.to_bytes(3, 'little')    

        representacao_binaria = ''.join(format(byte, '08b') for byte in msg)
        print(representacao_binaria)       
        
        # Sock de enviando a mensagem para o servidor
        sock.sendto(msg, (UDP_IP, UDP_PORT))
        
        
        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)
        # Exibindo a mensagem em bytes do servidor e o endereco
        print(f"Mensagem do Servidor: {msg_server}")
        print(f"Endereco: {addr}")
        # Mensagem em binario do servidor
        representacao_binaria = ''.join(format(byte, '08b') for byte in msg_server)
        print(representacao_binaria)    
        # Tipo de mensagem
        requisidor.receber_resposta(int.from_bytes(msg_server, byteorder='little'))

    elif op == 4:   
        break
    else:
        print("OPCAO INVALIDA!!!")



