import random
import sys

def gerar_requisicao(req_res, tipo, identificador):
    req_res = req_res & 0xF
    tipo = tipo & 0xF
    mensagem = ((((identificador << 4) | tipo) << 4) | req_res) & 0xFFFFFF
    
    return mensagem
    
def random_id(): 
    return random.randint(0, 65535)

def receber_resposta(mensagem):
    req_res = mensagem & 0xF
    tipo = (mensagem >> 4) & 0xF
    identificador = (mensagem >> 8) & 0xFFFF

    tamanho = (mensagem >> 24) & 0xFF
    caractere = chr((mensagem >> 32) & 0xFF)

    for i in range(tamanho):
        caractere = chr((mensagem >> 32+(i*8)) & 0xFF)
        print(caractere)



