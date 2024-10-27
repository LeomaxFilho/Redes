import heads
import request_response
from scapy.compat import raw
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1 

while(True):   
    op = int(input("[1] Data e Hora\n[2] Mensagem Motivacional\n[3] Respostas Emitidas\n[4] Sair: "))
    
    # Gerar o identificador
    identficador = request_response.random_id()

    # * Data e hora
    if op == 1:

        # Gera a mensagem para ser enviada para o servidor
        packet = heads.scapy_udp(0,0,identficador)
                
        # Envio e tratamento da mensagem 
        packet_server = sr1(packet, verbose=0)
        msg_server = packet_server.lastlayer()
        msg_server = raw(msg_server)

        # Tipo de mensagem do servidor
        request_response.receber_resposta(int.from_bytes(msg_server, byteorder='little'))


    # * Mensagem motivacional
    elif op == 2:
       # Gera a mensagem para ser enviada para o servidor
        packet = heads.scapy_udp(0,1,identficador)
        
        # Envio e tratamento da mensagem 
        packet_server = sr1(packet, verbose=0) 
        msg_server = packet_server.lastlayer() 
        msg_server = raw(msg_server)
        
        # Tipo de mensagem do servidor
        request_response.receber_resposta(int.from_bytes(msg_server, byteorder='little'))


    # * Mensagem de quantidade de requisicoes
    elif op == 3:
        # Gera a mensagem para ser enviada para o servidor
        packet = heads.scapy_udp(0,2,identficador)
                
        packet_server = sr1(packet, verbose=0)
        msg_server = packet_server.lastlayer()
        msg_server = raw(msg_server)
        
        # Tipo de mensagem do servidor
        request_response.receber_resposta_int(int.from_bytes(msg_server, byteorder='little'))

    elif op == 4:   
        break
    else:
        print("OPCAO INVALIDA!!!")
