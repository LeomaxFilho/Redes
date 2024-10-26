import random
from scapy.all import *

def gerar_requisicao(req_res, tipo, identificador):
    req_res = req_res & 0xF
    tipo = tipo & 0xF
    mensagem = ((((identificador << 4) | req_res) << 4) |  tipo ) & 0xFFFFFF
    return mensagem
    
def random_id(): 
    return random.randint(0, 65535)

def receber_resposta(mensagem):

    tamanho = (mensagem >> 24) & 0xFF
    caractere = ''

    for i in range(tamanho):
        caractere += chr((mensagem >> 32+(i*8)) & 0xFF)
    
    print(caractere)

def receber_resposta_int(mensagem):

    caractere = (mensagem >> 32)

    entra = caractere.to_bytes(4, byteorder='little')
    sai = int.from_bytes(entra, byteorder='big')

    print(sai)

def process_packet(packet):
    if packet.haslayer(UDP):
        print("Pacote UDP recebido:", packet.summary())
