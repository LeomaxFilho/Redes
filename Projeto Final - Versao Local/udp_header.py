import struct
import request_response
from scapy.compat import raw
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1 

# Pseudo Cabecalho do IP
def ipBytes(IP):
    ipFinish = 0
    
    # adiciona os bytes separados a um vetor
    oct = IP.split('.')
    ipBytes = []

    for number in oct:
        ipBytes.append(int(number))

    for i in range(len(ipBytes)):
        ipFinish = (ipFinish << 8) | (ipBytes[i] & 0xFF)

    saida = ipFinish.to_bytes(4, byteorder='little') #coloca no tipo bytes

    return saida

# Calculo do checkSum
def checksumUdp(udpSegment, sourceIp, desIp):

    tempHeader = struct.pack("!4s4sBBH", sourceIp, desIp, 0, 17, len(udpSegment))

    cheksumData = tempHeader + udpSegment
    
    soma = 0
    for i in range(0, len(cheksumData), 2):
        parte = (cheksumData[i] << 8) + (cheksumData[i + 1] if i + 1 < len(cheksumData) else 0)
        soma += parte
        soma = (soma & 0xFFFF) + (soma >> 16)
    
    checksum = ~soma & 0xFFFF

    return checksum

# Cabecalho do UDP
def udpHead(sourceIp, desIp, sourcePort, desPort, comprimento, data):

    noCheksum = struct.pack("!HHHH", sourcePort, desPort, comprimento, 0)

    udpSegment = noCheksum + data

    checksum = checksumUdp(udpSegment, sourceIp, desIp)
    
    udpFinish = struct.pack("!HHHH", sourcePort, desPort, comprimento, checksum)
    
    return udpFinish

# Preparacao do pacote com o preenchimento adequado do cabecalho
def scapy_udp(req, tipo, identificador):
    # Parametro de referencia
    sourceIp = ipBytes('192.168.1.102')
    desIp = ipBytes('15.228.191.109')
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
    scapy_packet = IP(dst='15.228.191.109')/UDP(dport=scapy_dstPort, sport=scapy_srcPort, len=scapy_len )/data # Probleminha no checksum 
    
    ''', chksum=scapy_checksum, len=scapy_len)'''

    return scapy_packet

