from audioop import add
import json
import socket

from datetime import datetime


now = datetime.now()

horario_criacao = now.strftime("%H:%M:%S")

localIP = "192.168.0.10"

localPort = 20001

bufferSize = 1024

# criando o socket pra receber

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# add o ip e a porta no socket

UDPServerSocket.bind((localIP, localPort))

print("UDP server ouvindo")
print("Servidor criado as: " + horario_criacao)

json_envio = {}
json_server = {}


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
                                'ACK': "true"}



    str_encoded = json.dumps(json_envio).encode(encoding = 'UTF-8')

    # mandando de volta pro client
    UDPServerSocket.sendto(str_encoded, address)

    msgFromServer = input("Mensagem para o cliente: ")

    json_server ['send'] = {'ip_origem': localIP, 
                             'ip_destino': clientIP, 
                             'porta_origem': localPort, 
                             'porta_destino': clientPort, 
                             'timestamp_msg_original': time_client, 
                             'timestamp_msg_resposta': current_time,
                             'msg_client': clientMsg,
                             'msg_server': msgFromServer}

    str_server = json.dumps(json_server).encode(encoding = 'UTF-8')

    bytesClient = str.encode(json.dumps(json_server))



    bufferSize = 1024

    #criando o udp socket do client

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    clientAddressPort = (clientIP, clientPort)
    #mandando para o servidor usando udp socket

    UDPClientSocket.sendto(bytesClient, clientAddressPort)
    


