import socket
import requisidor

# Especificacoes do servidor 
UDP_IP = "15.228.191.109"
UDP_PORT = 50000

# Criacao do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):   
    op = int(input(print("[1] Data e Hora\n[2] Mensagem Motivacional\n[3] Respostas Emitidas\n[4] Sair: ")))
    
    if op == 1:
        
        # Gera o identificador
        identficador = requisidor.random_id()
        
        # Gera a mensagem para ser enviada para o servidor
        req = requisidor.gerar_requisicao(0, 0, identficador)

        # Exibicao correta da mensagem de requisicao
        print(bin(req))
        print(type(req))

        # Essa conversao ta formatando errado a mensagem
        mensagem = str(req)

        # Ferramente para exibir o conteudo no formato binario do Gepeto    
        binary_representation = ''.join(format(ord(char), '08b') for char in mensagem)
        print(binary_representation)

        # Sock de enviando a mensagem para o servidor
        sock.sendto(mensagem.encode(), (UDP_IP, UDP_PORT))

        # Recebendo a mensagem do servidor
        msg_server, addr = sock.recvfrom(1024)

        print(f"Mensagem do Servidor: {msg_server}")
        print(f"Endereco: {addr}")

        representacao_binaria = ''.join(format(byte, '08b') for byte in msg_server)

        print(representacao_binaria)    



    elif op == 2:
        identficador = requisidor.random_id()
        mensagem = requisidor.gerar_requisicao(0, 1, identficador)
        print(bin(mensagem))
    elif op == 3:  
        identficador = requisidor.random_id()
        mensagem = requisidor.gerar_requisicao(0, 2, identficador)
        print(bin(mensagem))
    elif op == 4:   
        break
    else:
        print("OPCAO INVALIDA!!!")