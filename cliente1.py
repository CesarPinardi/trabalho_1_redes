import json
import socket
from datetime import datetime
from traceback import print_tb
import time

# horario atual
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

# ip de destino (servidor)
ip_dest = input("IP do servidor: ")

# msg a ser enviada do client para o server
msgFromClient = input("Mensagem para o servidor: ")

# ip e porta locais
port = 20001

ip = "192.168.0.11"

# bind
serverAddressPort = (ip_dest, port)

port_dest = 20001

json_envio = {}

# json a ser enviado
json_envio ['info_to_sent'] = {'ip_origem': ip, 
                            'ip_destino': ip_dest, 
                            'porta_origem': port, 
                            'porta_destino': port_dest, 
                            'timestamp': current_time, 
                            'msg': msgFromClient}
# json para bytes
bytesToSend = str.encode(json.dumps(json_envio))

bufferSize = 1024

#criando o udp socket do client

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#mandando para o servidor usando udp socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
 
# recebendo a resposta do servidor 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#transformar message para string
msgFromServer_tostring = msgFromServer[0].decode()

#transformar message para json
json_server = json.loads(msgFromServer_tostring)

# vendo se o ack = true ou seja, foi confirmado o recebimento
ack = json_server.get("received").get("ACK")

# print do json com ack
print("\nMensagem de confirmação: \n" + (json.dumps(json_server.get("received"), indent= len(json_server.get("received")))))

if ack:
    # print do json com a msg do server
    print("\nMensagem do servidor: \n" + (json.dumps(json_server.get("send"), indent= len(json_server.get("send")))))


print("\n")
