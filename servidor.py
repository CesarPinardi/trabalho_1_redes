from audioop import add
import json
import socket
from datetime import datetime

# pegando horario atual para a criacao do server

now = datetime.now()

horario_criacao = now.strftime("%H:%M:%S")

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

# criando o socket pra receber

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# add o ip e a porta no socket

UDPServerSocket.bind((localIP, localPort))

# print para reconhecimento que o servidor foi criado
print("UDP server ouvindo")
print("Servidor criado as: " + horario_criacao)

# talvez tenha que criar o json aqui fora antes de referenciar la dentro?

while(True):
    # pegando horario atual para a resposta
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    # recebendo a resposta do cliente 
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    # referenciando a resposta (array)
    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    #transformar message para string
    msg_em_string = message.decode()
    
    #transformar message para json
    json_client = json.loads(msg_em_string)

    print("Recebido pelo cliente\n")

    print((json.dumps(json_client.get("info_to_sent"), indent= len(json_client.get("info_to_sent")))))

    print("\n")

    # acessando as keys do json
    clientMsg = json_client.get("info_to_sent").get("msg")

    clientIP  = json_client.get("info_to_sent").get("ip_origem")

    clientPort = json_client.get("info_to_sent").get("porta_origem")
    
    time_client = json_client.get("info_to_sent").get("timestamp")

    msgfromserver = input("Msg para o cliente: ")

    # ao inves de 2 jsons, um array de jsons com os dois, um com ack e outro com msg desse servidor

    json_full = {
        "received": {
            'ip_origem': localIP, 
            'ip_destino': clientIP, 
            'porta_origem': localPort, 
            'porta_destino': clientPort, 
            'timestamp_msg_original': time_client, 
            'timestamp_msg_resposta': current_time,
            'ACK': True
            },

        "send": {
            'ip_origem': localIP, 
            'ip_destino': clientIP, 
            'porta_origem': localPort, 
            'porta_destino': clientPort, 
            'timestamp_msg_original': time_client, 
            'timestamp_msg_resposta': current_time,
            'msg_client': clientMsg,
            'msg_server': msgfromserver
            }
    }
    
    # transformando o json array em bytes
    str_encoded = json.dumps(json_full).encode(encoding = 'UTF-8')
    
    # mandando de volta pro client
    UDPServerSocket.sendto(str_encoded, address)


    

