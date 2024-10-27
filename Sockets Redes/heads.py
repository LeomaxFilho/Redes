'''
LUIS ALVES DE PAIVA NETO
LEOMAX DA COSTA BANDEIRA FILHO
'''

import struct
from scapy.compat import raw # type: ignore
from scapy.layers.inet import IP, UDP # type: ignore
from scapy.sendrecv import sr1  # type: ignore
import request_response

# Pseudo cabecalho do IP
def ipBytes(IP):
    ipFinish = 0
    
    # adiciona os bytes separados a um vetor
    oct = IP.split('.')
    ipBytes = []

    for number in oct:
        ipBytes.append(int(number))

    for i in range(len(ipBytes)):
        ipFinish = (ipFinish << 8) | (ipBytes[i] & 0xFF)

    saida = ipFinish.to_bytes(4, byteorder='little') # coloca no tipo bytes

    return saida

# Calculo do checksum
def checksum(data):
    if len(data) % 2 == 1:
        data += b'\x00'  # Se o tamanho for impar
    
    sum = 0
    for i in range(0, len(data), 2): # Para ir de dois em dois
        word = (data[i] << 8) + data[i + 1]  # Combina dois bytes em um bloco de 16 bits
        sum += word
        sum = (sum & 0xFFFF) + (sum >> 16)  # Adiciona o carry ao final

    return ~sum & 0xFFFF  # Retorna o complemento de um

# Calculo do checksum completo
def udp_checksum(src_addr, dest_addr, src_port, dest_port, data):
    # Pseudo-cabeçalho
    src_addr = ipBytes(src_addr)
    dest_addr = ipBytes(dest_addr)
    placeholder = 0
    protocol = 17  # Protocolo UDP
    udp_length = 8 + len(data)  # Cabeçalho UDP (8 bytes) + dados

    pseudo_header = struct.pack('!4s4sBBH', src_addr, dest_addr, placeholder, protocol, udp_length)

    # Cabeçalho UDP
    udp_header = struct.pack('!HHHH', src_port, dest_port, udp_length, 0)

    # Dados UDP
    udp_packet = pseudo_header + udp_header + data

    return checksum(udp_packet)

# Calculo do cabecalho
def udpHead(sourceIp, desIp, sourcePort, desPort, comprimento, data):

    noCheksum = struct.pack("!HHHH", sourcePort, desPort, comprimento, 0)

    udpSegment = noCheksum + data

    checksum = udp_checksum(sourceIp, desIp, sourcePort, desPort, data)
    
    udpFinish = struct.pack("!HHHH", sourcePort, desPort, comprimento, checksum)
    
    return udpFinish


# Preparacao do pacote com o preenchimento adequado do cabecalho
def scapy_udp(req, tipo, identificador):
    # Parametro de referencia
    sourceIp = '172.25.10.126'
    desIp = '15.228.191.109'
    sourcePort = 59155
    desPort = 50000

    # Mensagem de requisicao
    requisicao = request_response.gerar_requisicao(req ,tipo , identificador)
    data = requisicao.to_bytes(3, 'little')

    comprimento = 8 + len(data) # o 8 vem do cabecalho fixo

    # Cabecalho UDP
    udpHeader = udpHead(sourceIp, desIp, sourcePort, desPort, comprimento, data)
    udpHeader = int.from_bytes(udpHeader, byteorder='big')

    # Valor da implementacao do cabecalho
    scapy_srcPort = (udpHeader >> 48) & 0xFFFF
    scapy_dstPort = (udpHeader >> 32) & 0xFFFF
    scapy_len = (udpHeader >> 16) & 0xFFFF
    scapy_checksum = udpHeader & 0xFFFF

    # Preparando o pacote para envio
    scapy_packet = IP(dst='15.228.191.109')/UDP(dport=scapy_dstPort, sport=scapy_srcPort, len=scapy_len)/data  
    
    return scapy_packet