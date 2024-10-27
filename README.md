# Projeto de Comunicação UDP com Sockets e Scapy

## Introdução

Este projeto implementa uma aplicação de rede usando o protocolo UDP e a biblioteca Scapy para envio e recebimento de pacotes em Python. O **UDP (User Datagram Protocol)** é um protocolo de transporte sem conexão, o que significa que não estabelece uma conexão antes de transmitir dados. Isso o torna ideal para aplicações que priorizam velocidade em vez de confiabilidade total. Para manipulação de pacotes, o projeto utiliza **sockets** e **Scapy**, uma biblioteca poderosa para construção e manipulação de pacotes de rede personalizados.

## Estrutura dos Arquivos

1. **`request_response.py`**: Define funções para criação e processamento de requisições e respostas.
2. **`socket_scapy.py`**: Usa Scapy para enviar pacotes UDP com cabeçalhos customizados.
3. **`socket_udp.py`**: Utiliza a biblioteca padrão de sockets para comunicação UDP.
4. **`heads.py`**: Contém funções de criação de cabeçalhos IP e UDP e para cálculo de checksum dos pacotes.

## Configuração e Execução

### Requisitos

- Python 3.8 ou superior
- Biblioteca Scapy (`pip install scapy`)

### Executando a Aplicação

O projeto oferece duas opções para envio de pacotes:

- **socket_udp.py**: Usa a biblioteca padrão `socket`.
- **socket_scapy.py**: Usa a biblioteca `Scapy`.

### Estrutura e Funcionamento do Código

#### 1. `request_response.py`

Este módulo gera e processa mensagens para envio e recebimento.

- **`gerar_requisicao(req_res, tipo, identificador)`**: Cria uma requisição com base no tipo e identificador fornecidos.
- **`random_id()`**: Gera um identificador aleatório.
- **`receber_resposta(mensagem)`**: Processa e exibe a mensagem recebida como caracteres.
- **`receber_resposta_int(mensagem)`**: Processa a mensagem recebida e a converte em número inteiro.

#### 2. `socket_udp.py`

Utiliza sockets para envio e recebimento de pacotes UDP.

- Cria um socket UDP e se conecta ao servidor definido em `UDP_IP` e `UDP_PORT`.
- Gera uma requisição usando `gerar_requisicao` e envia a mensagem codificada.
- Recebe a resposta do servidor e a processa com `receber_resposta` ou `receber_resposta_int`, dependendo do tipo de requisição (data/hora, mensagem motivacional ou número de respostas emitidas).

#### 3. `socket_scapy.py`

Utiliza Scapy para construção e envio de pacotes UDP com cabeçalhos personalizados.

- Usa a função `scapy_udp` (definida em **heads.py**) para criar um cabeçalho IP e UDP com checksums calculados.
- Envia o pacote ao servidor usando `sr1`, que captura a resposta do servidor.
- Processa a resposta da mesma maneira que o `socket_udp.py`.

#### 4. `heads.py`

Define funções para construção de cabeçalhos e cálculo de checksum.

- **`ipBytes(IP)`**: Converte o IP em um array de bytes.
- **`checksum(data)`**: Calcula o checksum para verificação de integridade dos pacotes.
- **`udp_checksum(src_addr, dest_addr, src_port, dest_port, data)`**: Gera o checksum de um pacote UDP.
- **`udpHead`**: Constrói o cabeçalho UDP com o checksum.
- **`scapy_udp(req, tipo, identificador)`**: Constrói um pacote completo IP/UDP para envio contendo a requisição codificada.

### Exemplo de Uso

Para executar a aplicação com sockets nativos:

```bash
python socket_udp.py
```

Para executar a aplicação com Scapy:

```bash
python socket_scapy.py
```
A aplicação permite as seguintes opções de requisição:
1. Data e Hora
2. Mensagem Motivacional
3. Numero de Respostas Emitidas

## Referências
* [Documentação da Scapy](https://scapy.readthedocs.io/): Para manipulação de pacotes.
* [Biblioteca Socket em Python](https://docs.python.org/3/library/socket.html): Para comunicação em rede.

## Autores
* Luis Alves de Paiva Neto
* Leomax da Costa Bandeira Filho
