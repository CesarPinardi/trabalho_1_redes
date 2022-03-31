from audioop import add
import json
import socket

from datetime import datetime


now = datetime.now()

horario_criacao = now.strftime("%H:%M:%S")

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msgFromServer = "Ola cliente UDP"

bytesToSend = str.encode(msgFromServer)

# criando o socket pra receber

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# add o ip e a porta no socket

UDPServerSocket.bind((localIP, localPort))

print("UDP server ouvindo")
print("Servidor criado as: " + horario_criacao)

json_envio = {}

msg_para_client = 'Mensagem recebida!'

# Listen for incoming datagrams

while(True):
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")


    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]


    #transformar message para string
    msg_em_string = message.decode()
    
    #transformar message para json
    json_client = json.loads(msg_em_string)

    #acessando o json

        # print("\nMensagem do cliente: " + json_client.get("info_to_sent").get("msg"))

        # print("\nAgora: " + json_client.get("info_to_sent").get("timestamp"))

        # print("\nRequest recebido as: " + current_time)

        # print("\nIP cliente: " + json_client.get("info_to_sent").get("ip_origem"))

    print((json.dumps(json_client.get("info_to_sent"), indent= len(json_client.get("info_to_sent")))))

    print("\n")

    clientMsg = json_client.get("info_to_sent").get("msg")

    clientIP  = json_client.get("info_to_sent").get("ip_origem")

    clientPort = json_client.get("info_to_sent").get("porta_origem")
    
    time_client = json_client.get("info_to_sent").get("timestamp")

    json_envio ['received'] = {'ip_origem': localIP, 
                                'ip_destino': clientIP, 
                                'porta_origem': localPort, 
                                'porta_destino': clientPort, 
                                'timestamp_msg_original': time_client, 
                                'timestamp_msg_resposta': current_time,
                                'mensagem_original': clientMsg,
                                'mensagem_servidor': msg_para_client}


    str_encoded = json.dumps(json_envio).encode(encoding = 'UTF-8')

    # mandando de volta pro client

    UDPServerSocket.sendto(str_encoded, address)
