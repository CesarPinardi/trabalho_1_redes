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

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
print("Servidor criado as: " + horario_criacao)


json_envio = {}

msg_para_client = 'teste'

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
    json_object = json.loads(msg_em_string)

    #acessando o json

    print("Mensagem do cliente: " + json_object.get("info_to_sent").get("msg"))

    print("Agora: " + json_object.get("info_to_sent").get("timestamp"))

    print("Request recebido as: " + current_time)



    clientMsg = "Mensagem do cliente: {}".format(message)

    clientIP  = "IP do cliente: {}".format(address)

    clientPort = (address[9:len(address)])
    
    print(clientIP)

    time_client = 0

    json_envio ['received'] = {'ip_origem': localIP, 
                                'ip_destino': clientIP, 
                                'porta_origem': localPort, 
                                'porta_destino': clientPort, 
                                'timestamp_msg_original': time_client, 
                                'timestamp_msg_resposta': current_time,
                                'mensagem_original': clientMsg,
                                'msg': msg_para_client}


    str_encoded = json.dumps(json_envio).encode(encoding = 'UTF-8')


    # Sending a reply to client

    UDPServerSocket.sendto(str_encoded, address)
